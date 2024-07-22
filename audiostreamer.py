import logging
import subprocess
import pyaudio
import yt_dlp
import threading
import numpy as np
import time
import queue
from contextlib import contextmanager
from logging.handlers import RotatingFileHandler
import multiprocessing


########################################################################
################################# LOGS #################################
########################################################################

# Configure logging
logger = logging.getLogger('AudioStreamerLogger')
logger.setLevel(logging.INFO)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler('audiostreamer.log', maxBytes=1*1024*1024*1024, backupCount=1)

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

########################################################################
############################ AUDIOSTREAMER #############################
########################################################################

class AudioStreamer:
    def __init__(self, chunk_size=1024, channels=2, sample_rate=48000, volume=10.):
        # Audio Properties
        self.chunk_size = chunk_size
        self.channels = channels
        self.sample_rate = sample_rate
        self.set_volume(volume)
        # Initialize PyAudio and Stream
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.sec_per_chunk = chunk_size / (channels * sample_rate * 2) # 16-bit PCM audio - 2 Bytes per Sample
        # Control Variables
        self.queue = []
        self.streamplayer_running = False
        self.is_playing = False
        self.is_paused = False
        self.pause_stream_player = threading.Event()
        self.new_track_position = None
    
    ########################################################################
    ############################ MANAGE STREAM #############################
    ########################################################################

    def open_stream(self):
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=self.channels,
                                  rate=self.sample_rate,
                                  output=True)
        logger.info('Stream Opened')
    
    def close_stream(self):
        self.is_playing = False
        try:
            if self.stream:
                if self.stream.is_active():
                    self.stream.stop_stream()
                self.stream.close()
                self.stream = None
                logger.info('Stream Closed')
        except Exception as e:
            logger.error(f"Error in Close Stream: {e}")
    
    def terminate_audiostreamer(self):
        self.streamplayer_running = False
        self.pause_stream_player.set()
        if self.is_playing:
            self.is_playing = False
        else:
            self.close_stream()
        while self.stream:
            time.sleep(0.2)
        self.p.terminate()
        logger.info('Audiostreamer Terminated')
    
    ########################################################################
    ########################### STREAM COMMANDS ############################
    ########################################################################

    def add_track(self, track):
        try:
            self.queue.append(track)
            logger.info(f'Song Added to Queue')
            if self.queue and not self.pause_stream_player.is_set():
                self.pause_stream_player.set()
                logger.info(f'Resume Stream Player')
        except Exception as e:
            logger.error(f"Error in Add Song: {e}")

    def set_volume(self, volume):
        try:
            self.volume = np.clip(volume/100, 0, 1)
            logger.info(f'Volume set to {self.volume*100}')
        except Exception as e:
            logger.error(f"Error in Volume Setting: {e}")
    
    def set_position(self, position):
        if self.is_playing:
            track_duration = self.queue[0]['duration']
            if position >= 0 and position <= track_duration:
                self.new_track_position = position
                self.is_playing = False
            else:
                logger.error(f"Error in Set Position: {position} outside of bounds - [0, {track_duration}]")
    
    def pause(self):
        try:
            if self.is_playing:
                if not self.is_paused:
                    self.is_paused = True
                    self.stream.stop_stream()
                    logger.info(f'Stream Paused')
        except Exception as e:
            logger.error(f"Error in Pause: {e}")
    
    def resume(self):
        try:
            if self.is_playing:
                if self.is_paused:
                    self.stream.start_stream()
                    self.is_paused = False
                    logger.info(f'Stream Resumed')
        except Exception as e:
            logger.error(f"Error in Resume: {e}")
    
    def skip(self):
        if self.queue:
            self.is_playing = False
            logger.info(f'Song Skip')

    ########################################################################
    ############################ STREAM PLAYER #############################
    ########################################################################

    def stream_player(self):
        logger.info('Create Stream Player')
        self.streamplayer_running = True
        while self.streamplayer_running:
            self.pause_stream_player.wait() # Will block if self.pause_stream_player is cleared
            if self.queue:
                self.play(self.queue[0])
                self.queue = self.queue[1:]
                self.is_paused = False
            else:
                #time.sleep(0.5)
                if self.pause_stream_player.is_set():
                    self.pause_stream_player.clear()
                    logger.info(f'Pause Stream Player')
        logger.info('Stream Player Closed')

    @staticmethod
    @contextmanager
    def managed_subprocess(command):
        logger.info('Starting Process')
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # import ffmpeg
        # process = (
        #     ffmpeg
        #     .input(url)
        #     .output('pipe:', format='s16le', ac=self.channels, ar=self.sample_rate)
        #     .run_async(pipe_stdout=True, pipe_stderr=True)
        # )
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

    def play(self, track, position=0):
        logger.info('Starting Stream')
        self.is_playing = True
        self.open_stream()
        chunk_buffer = queue.Queue(maxsize=600/self.sec_per_chunk) # number of chunks for 10 minutes
        
        ffmpeg_command = [
            'ffmpeg',
            '-loglevel', 'error',
            '-ss', str(position),
            '-i', track['url'],
            '-f', 's16le',
            '-ac', str(self.channels),
            '-ar', str(self.sample_rate),
            '-'
        ]

        # Stop Event for Result Thread
        stop_event_ffmpeg_thread = threading.Event()

        def read_ffmpeg_output():
            with self.managed_subprocess(ffmpeg_command) as process:
                while not stop_event_ffmpeg_thread.is_set():
                    chunk = process.stdout.read(self.chunk_size)
                    if chunk:
                        chunk_buffer.put(chunk)
                    else:
                        chunk_buffer.put(None)
                        break
            logger.info('ffmpeg Thread Exiting')

        # Thread to Read ffmpeg Output
        ffmpeg_thread = threading.Thread(target=read_ffmpeg_output, daemon=True)
        ffmpeg_thread.start()

        try:
            while self.is_playing:

                if self.is_paused:
                    time.sleep(0.3)
                    continue
                
                chunk = chunk_buffer.get(timeout=3)
                if chunk:
                    audio_data = np.frombuffer(chunk, dtype=np.int16)
                    audio_data = np.clip(audio_data * self.volume, -32768, 32767).astype(np.int16)
                    self.stream.write(audio_data.tobytes())
                else:
                    logger.info('End of audio stream reached')
                    break
        except queue.Empty:
            logger.error(f"Error during audio streaming: Chunk Buffer Empty for 5 seconds")
        except Exception as e:
            logger.error(f"Error during audio streaming: {e}")
        finally:
            self.is_playing = False
            stop_event_ffmpeg_thread.set()
            if chunk_buffer.full():
                chunk_buffer.get()
            ffmpeg_thread.join()
            del chunk_buffer # ?
            self.close_stream()
        
        if self.new_track_position:
            new_track_position = self.new_track_position
            self.new_track_position = None
            logger.info(f'Position set to {new_track_position}')
            self.play(track, position=new_track_position)


########################################################################
############################### YDL URL ################################
########################################################################

def get_youtube_audio_url(url):
    ydl_opts = {
        'format': 'bestaudio',
        'noplaylist': True,
        'quiet': True,
        'extract_flat': 'in_playlist',
        }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            audio_url = info_dict['url']
            duration = int(info_dict['duration'])
        logger.info('Youtube Audio URL Obtained')
        return audio_url, duration
    except Exception as e:
        logger.error(f"Error in Obtaining Youtube Audio URL: {e}")
        return 0, 0
    
########################################################################
################################# MAIN #################################
########################################################################

def result_handler(async_results, streamer, pause_event, stop_event):
    logger.info('Start Result Handler Thread')
    while not stop_event.is_set():
        time.sleep(1)
        if not async_results:
            pause_event.clear()
            logger.info('Result Handler Thread Paused')
        pause_event.wait()  # Will block if pause_event is cleared
        for result in async_results:
            if result.ready():
                try:
                    audio_url, duration = result.get()
                    if audio_url:
                        track = {'url': audio_url,
                                'duration': duration}
                        streamer.add_track(track)
                except Exception as e:
                    logger.error(f"Error fetching audio URL from Worker Process: {e}")
                async_results.remove(result)
    logger.info('Result Handler Thread Exiting')

if __name__ == "__main__":
    logger.info('START Script')

    STREAMER = AudioStreamer()
    
    streaming_thread = threading.Thread(target=STREAMER.stream_player, daemon=True)
    streaming_thread.start()

    # Create a multiprocessing Pool for handling URL fetching
    with multiprocessing.Pool(processes=1) as pool:
        async_results = []

        # Pause Event for Result Thread
        pause_event = threading.Event()

        # Stop Event for Result Thread
        stop_event = threading.Event()

        # Start a thread to handle results
        result_thread = threading.Thread(target=result_handler, args=(async_results, STREAMER, pause_event, stop_event), daemon=True)
        result_thread.start()

        try:
            while True:
                command = input("Enter command (a/s/p/r/v/q): ")
                if command.lower().startswith("a"):
                    _, url = command.split()
                    logger.info('Youtube URL Obtained')
                    result = pool.apply_async(get_youtube_audio_url, (url,))
                    async_results.append(result)
                    if async_results and not pause_event.is_set():
                        pause_event.set()
                        logger.info('Result Handler Thread Resumed')
                elif command.lower() == "s":
                    STREAMER.skip()
                elif command.lower() == "p":
                    STREAMER.pause()
                elif command.lower() == "r":
                    STREAMER.resume()
                elif command.lower().startswith("v"):
                    _, vol = command.split()
                    STREAMER.set_volume(float(vol))
                elif command.lower().startswith("sp"):
                    _, pos = command.split()
                    STREAMER.set_position(int(pos))
                elif command.lower() == "q":
                    raise KeyboardInterrupt
                else:
                    print("Unknown command. Use 'a', 's', 'p', 'r', 'v', 'sp', or 'q'")       
        except KeyboardInterrupt:
            logger.info('Keyboard interrupt received')
        finally:
            pause_event.set()
            stop_event.set()
            result_thread.join()
            STREAMER.terminate_audiostreamer()
            streaming_thread.join()
            pool.close()
            pool.join()
            logger.info('EXIT Script')
