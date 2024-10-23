import subprocess
import yt_dlp
import threading
import numpy as np
import time
import queue
from contextlib import contextmanager
from logging.handlers import RotatingFileHandler
import multiprocessing
import sounddevice as sd


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
        # Initialize Stream
        self.stream = None
        self.sec_per_chunk = chunk_size / (channels * sample_rate * 2) # 16-bit PCM audio - 2 Bytes per Sample
        self.max_buffersize = 600/self.sec_per_chunk # number of chunks for 10 minutes (buffersize)
        # Control Variables
        self.queue = []
        self.is_playing = False
        self.is_paused = False
        self.new_position = False
    
    ########################################################################
    ############################ MANAGE STREAM #############################
    ########################################################################

    def open_stream(self):
        self.stream = sd.OutputStream(samplerate=48000, channels=2, dtype='int16')
        self.stream.start()
        print('Stream Opened')
    
    def close_stream(self):
        self.is_playing = False
        try:
            if self.stream:
                self.stream.stop()
                self.stream.close()
                self.stream = None
                print('Stream Closed')
        except Exception as e:
            print(f"Error in Close Stream: {e}")
    
    def terminate_audiostreamer(self):
        if self.is_playing:
            self.is_playing = False
        else:
            self.close_stream()
        while self.stream:
            time.sleep(0.2)
        print('Audiostreamer Terminated')
    
    ########################################################################
    ########################### STREAM COMMANDS ############################
    ########################################################################

    def add_track(self, track):
        try:
            self.queue.append(track)
            print(f'Song Added to Queue')
            if not self.is_playing:
                self.play()
                
        except Exception as e:
            print(f"Error in Add Song: {e}")

    def set_volume(self, volume):
        try:
            self.volume = np.clip(volume/100, 0, 1)
            print(f'Volume set to {int(self.volume*100)}')
        except Exception as e:
            print(f"Error in Volume Setting: {e}")
    
    def set_position(self, position):
        if self.is_playing:
            track_duration = self.queue[0]['duration']
            if position >= 0 and position <= track_duration:
                self.queue[0]['position'] = position
                self.new_position = True
                self.is_playing = False
            else:
                print(f"Error in Set Position: {position} outside of bounds - [0, {track_duration}]")
    
    def pause(self):
        try:
            if self.is_playing:
                if not self.is_paused:
                    self.is_paused = True
                    self.stream.stop()
                    print(f'Stream Paused')
        except Exception as e:
            print(f"Error in Pause: {e}")
    
    def resume(self):
        try:
            if self.is_playing:
                if self.is_paused:
                    self.stream.start()
                    self.is_paused = False
                    print(f'Stream Resumed')
        except Exception as e:
            print(f"Error in Resume: {e}")
    
    def skip(self):
        if self.queue:
            self.is_playing = False
            print(f'Song Skip')

    ########################################################################
    ############################ STREAM PLAYER #############################
    ########################################################################

    @staticmethod
    @contextmanager
    def managed_subprocess(command):
        print('Starting Process')
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            yield process
        except Exception as e:
            print(f"Error in Process: {e}")
        finally:
            process.stdout.close()
            process.stderr.close()
            process.terminate()
            process.wait()
            print('Process Closed')

    def play(self, position=0):
        if not self.is_playing:
            threading.Thread(target=self.player_thread, args=(self.queue[0],position,), daemon=True).start()
        else:
            print(f'Player Already Playing')

    def player_thread(self, track, position):
        print('Player Thread Start')
        self.is_playing = True
        self.open_stream()
        chunk_buffer = queue.Queue(maxsize=self.max_buffersize)
        
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
            print('ffmpeg Thread Exiting')

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
                    audio_data = audio_data.reshape(-1,self.channels)
                    self.stream.write(audio_data)
                else:
                    print('End of audio stream reached')
                    break
        except queue.Empty:
            print(f"Error during audio streaming: Chunk Buffer Empty for 5 seconds")
        except Exception as e:
            print(f"Error during audio streaming: {e}")
        finally:
            self.close_stream()
            stop_event_ffmpeg_thread.set()
            if chunk_buffer.full():
                chunk_buffer.get()
            ffmpeg_thread.join()
            self.on_track_end()
        print('Player Thread Exiting')

    def on_track_end(self):
        if self.new_position:
            self.change_position()
        else:
            print('Track Ended')
            self.play_next_track()
    
    def change_position(self):
        self.play(position=self.queue[0]['position'])
        print(f'Position set to {self.queue[0]["position"]}')
        self.new_position= False

    def play_next_track(self):
        self.queue.pop(0)
        if self.queue:
            self.play()
        else:
            print('Queue Empty')
        


########################################################################
############################### YDL URL ################################
########################################################################

def get_youtube_audio_url(url):
    ydl_opts = {
        'format': 'bestaudio',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'extract_flat': 'in_playlist',
        }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            audio_url = info_dict['url']
            duration = int(info_dict['duration'])
        print('Youtube Audio URL Obtained')
        return audio_url, duration
    except Exception as e:
        print(f"Error in Obtaining Youtube Audio URL: {e}")
        return 0, 0
    
########################################################################
################################# MAIN #################################
########################################################################

def result_handler(async_results, streamer, pause_event, stop_event):
    print('Start Result Handler Thread')
    while not stop_event.is_set():
        time.sleep(1)
        if not async_results:
            pause_event.clear()
            print('Result Handler Thread Paused')
        pause_event.wait()  # Will block if pause_event is cleared
        for result in async_results:
            if result.ready():
                try:
                    audio_url, duration = result.get()
                    if audio_url:
                        track = {'url': audio_url,
                                'duration': duration,
                                'position': 0}
                        streamer.add_track(track)
                except Exception as e:
                    print(f"Error fetching audio URL from Worker Process: {e}")
                async_results.remove(result)
    print('Result Handler Thread Exiting')

if __name__ == "__main__":
    print('START Script')

    STREAMER = AudioStreamer()

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
                    print('Youtube URL Obtained')
                    result = pool.apply_async(get_youtube_audio_url, (url,))
                    async_results.append(result)
                    if async_results and not pause_event.is_set():
                        pause_event.set()
                        print('Result Handler Thread Resumed')
                elif command.lower() == "s":
                    STREAMER.skip()
                elif command.lower() == "p":
                    STREAMER.pause()
                elif command.lower() == "r":
                    STREAMER.resume()
                elif command.lower().startswith("v"):
                    _, vol = command.split()
                    STREAMER.set_volume(int(vol))
                elif command.lower().startswith("sp"):
                    _, pos = command.split()
                    STREAMER.set_position(int(pos))
                elif command.lower() == "q":
                    raise KeyboardInterrupt
                else:
                    print("Unknown command. Use 'a', 's', 'p', 'r', 'v', 'sp', or 'q'")       
        except KeyboardInterrupt:
            print('Keyboard interrupt received')
        finally:
            pause_event.set()
            stop_event.set()
            result_thread.join()
            STREAMER.terminate_audiostreamer()
            pool.close()
            pool.join()
            print('EXIT Script')
