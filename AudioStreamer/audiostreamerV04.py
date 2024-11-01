import subprocess
import threading
import numpy as np
import time
import queue
from contextlib import contextmanager
import sounddevice as sd
from .logger import logger
from .audiostreamertrack import AudioStreamerTrack
from .events import Event, TrackStartEvent, TrackEndEvent, TrackExceptionEvent


class AudioStreamer:
    """
    16-bit PCM audio - 2 Bytes per Sample
    Sample Rate of 48,000 Hz, the system captures 48,000 samples per second for each audio channel.
    Chunk Size, number of Bytes per iteration
    -----------------------------------------------------------------------------------------------
    ChunkSize/2 -> Total Number of Samples per iteration
    ChunkSize/2/Channels -> Number of Samples per channel per iteration
    ChunkSize/2/Channels/SampleRate = ChunkSize / (2 * Channels * SampleRate) -> Number of Seconds Per Chunk(iteration)
    """
    def __init__(self, chunk_size=1024, channels=2, sample_rate=48000, volume=10.):
        logger.info('-'*20+' AudioStreamerV04 Initialized '+'-'*20)
        # Audio Properties
        self._chunk_size = chunk_size
        self._channels = channels
        self._sample_rate = sample_rate
        self.set_volume(volume)
        # Initialize Stream
        self._stream = None
        # Auxiliar Variables 
        self._bytes_per_sample = 2 # 16-bit PCM audio - 2 Bytes per Sample
        self._sec_per_chunk = chunk_size / (channels * sample_rate * self._bytes_per_sample) 
        self._max_buffersize = 10*60/self._sec_per_chunk # number of chunks for 10 minutes (buffersize)
        # Status Variables
        self._active = False
        self._paused = False
        self._current_track = None
        self._current_position = 0 # in seconds
        # Events dictionary to store all events
        self._events = {
            TrackStartEvent: TrackStartEvent(),
            TrackEndEvent: TrackEndEvent(),
            TrackExceptionEvent: TrackExceptionEvent(),
        }


    ########################################################################
    ############################# Properties ###############################
    ########################################################################
    
    @property
    def active(self):
        """True if audiostreamer is active with, either playing or paused."""
        return self._active

    @property
    def paused(self):
        """True if audiostreamer is paused."""
        return self._paused
    
    @property
    def playing(self):
        """True if audiostreamer is active and not paused."""
        return self._active and not self._paused

    @property
    def volume(self):
        """current audiostreamer volume."""
        return self._volume

    @property
    def current_position(self):
        """current audiostreamer position in sseconds."""
        return self._current_position
    

    ########################################################################
    ############################# Add Events ###############################
    ########################################################################

    def add_event_hook(self, *hooks, event=None):
        """
        Register one or more event hoooks to an event.
        If event is not specified than the hook(s) will be registered to all events.
        """
        if event is not None and not issubclass(event, Event):
            logger.error('Error in Add Event Hook: Event parameter is not of type Event or None')
            raise TypeError('Event parameter is not of type Event or None')
        
        for hook in hooks:
            if not callable(hook):
                logger.error('Error in Add Event Hook: Hook is not callable')
                raise TypeError('Each hook must be callable')
        
        if event is None:
            for ASevent in self._events.values():
                for hook in hooks:
                    ASevent.register(hook)
        elif event in self._events:
            for hook in hooks:
                self._events[event].register(hook)
        else:
            logger.error('Error in Add Event Hook: Event not used in AudioStreamer')
            raise TypeError("Event not used in AudioStreamer")
        logger.info(f'Hook(s) added to {event.__name__ if event is not None else "all events"}')


    ########################################################################
    ############################ MANAGE STREAM #############################
    ########################################################################

    def _open_stream(self):
        self._stream = sd.OutputStream(samplerate=self._sample_rate, channels=self._channels, dtype='int16')
        self._stream.start()
        logger.info('Stream Opened')
    
    def _close_stream(self):
        self._current_position = 0
        self._active = False
        try:
            if self._stream:
                self._stream.stop()
                self._stream.close()
                self._stream = None
                self._current_track = None
                logger.info('Stream Closed')
        except Exception as e:
            logger.error(f"Error in Close Stream: {e}")
    
    ########################################################################
    ########################### STREAM COMMANDS ############################
    ########################################################################

    def play(self, track, position=0):
        try:
            if self.active:
                self.stop()
            self._current_track = track
            self._paused = False
            self._events[TrackStartEvent].emit()
            logger.info(f'Play Track')
            self._play(position)
        except Exception as e:
            logger.error(f"Error in Play Track: {e}")
    
    def pause(self):
        try:
            if self.playing:
                self._paused = True
                self._stream.stop()
                logger.info(f'Stream Paused')
        except Exception as e:
            logger.error(f"Error in Pause: {e}")
    
    def resume(self):
        try:
            if self.active and self.paused:
                self._stream.start()
                self._paused = False
                logger.info(f'Stream Resumed')
        except Exception as e:
            logger.error(f"Error in Resume: {e}")
    
    def stop(self):
        try:
            logger.info(f'Stop Player')
            self._active = False
            while self._stream:
                time.sleep(0.2)
        except Exception as e:
            logger.error(f"Error in Stop: {e}")
    
    def set_volume(self, volume):
        try:
            self._volume = np.clip(volume/100, 0, 1)
            logger.info(f'Volume set to {int(self._volume*100)}')
        except Exception as e:
            logger.error(f"Error in Volume Setting: {e}")
    
    def seek(self, position):
        try:
            if self.active:
                duration = self._current_track.duration
                if position >= 0 and position <= duration:
                    self.stop()
                    self._play(position)
                    logger.info(f'Position set to {position}')
                else:
                    logger.error(f"Error in Set Position: {position} outside of bounds - [0, {duration}]")
        except Exception as e:
            logger.error(f"Error in Seek Position: {e}")
    

    ########################################################################
    ############################ STREAM PLAYER #############################
    ########################################################################

    def _play(self, position):
        if not self.active:
            threading.Thread(target=self._player_thread, args=(self._current_track,position,), daemon=True).start()
        else:
            logger.info(f'Player Already Playing')

    @staticmethod
    @contextmanager
    def _managed_subprocess(command):
        logger.info('Starting Process')
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            yield process
        except Exception as e:
            logger.error(f"Error in Process: {e}")
        finally:
            process.stdout.close()
            process.stderr.close()
            process.terminate()
            process.wait()
            logger.info('Process Closed')

    def _player_thread(self, track, position):
        logger.info('Player Thread Start')
        self._active = True
        self._current_position = position
        self._open_stream()
        chunk_buffer = queue.Queue(maxsize=self._max_buffersize)
        
        ffmpeg_command = [
            'ffmpeg',
            '-loglevel', 'error',
            '-ss', str(position),
            '-i', track.url,
            '-f', 's16le',
            '-ac', str(self._channels),
            '-ar', str(self._sample_rate),
            '-'
        ]

        # Stop Event for Result Thread
        stop_event_ffmpeg_thread = threading.Event()

        def _read_ffmpeg_output():
            with self._managed_subprocess(ffmpeg_command) as process:
                while not stop_event_ffmpeg_thread.is_set():
                    chunk = process.stdout.read(self._chunk_size)
                    if chunk:
                        chunk_buffer.put(chunk)
                    else:
                        chunk_buffer.put(None)
                        break
            logger.info('ffmpeg Thread Exiting')

        # Thread to Read ffmpeg Output
        ffmpeg_thread = threading.Thread(target=_read_ffmpeg_output, daemon=True)
        ffmpeg_thread.start()

        try:
            while self.active:

                if self.paused:
                    time.sleep(0.3)
                    continue

                chunk = chunk_buffer.get(timeout=3)
                if chunk:
                    audio_data = np.frombuffer(chunk, dtype=np.int16)
                    audio_data = np.clip(audio_data * self._volume, -32768, 32767).astype(np.int16)
                    audio_data = audio_data.reshape(-1,self._channels)
                    self._stream.write(audio_data)
                    self._current_position += self._sec_per_chunk
                else:
                    logger.info('End of audio stream reached')
                    break

        except queue.Empty:
            logger.error(f"Error during audio streaming: Chunk Buffer Empty for 3 seconds")
            self._events[TrackExceptionEvent].emit()
        except Exception as e:
            logger.error(f"Error during audio streaming: {e}")
            self._events[TrackExceptionEvent].emit()
        finally:
            self._close_stream()
            self._events[TrackEndEvent].emit()
            stop_event_ffmpeg_thread.set()
            if chunk_buffer.full():
                chunk_buffer.get()
            ffmpeg_thread.join()
        logger.info('Player Thread Exiting')
