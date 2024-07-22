import pyaudio
import yt_dlp
import subprocess
import threading
import queue
import time

# Link of the video to be processed
video_link = "https://www.youtube.com/watch?v=TKkcsmvYTw4"

# Global variables for managing the FFmpeg process and seek time
process = None
seek_time = 0

def get_audio_url(url):
    ydl_opts = {
        'format': 'bestaudio',
        'noplaylist': True,
        'quiet': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        audio_url = info_dict['url']
    return audio_url

def start_ffmpeg_process(audio_url, seek_time):
    # Prepare ffmpeg command with seeking
    ffmpeg_command = [
        'ffmpeg',
        '-loglevel', 'error',
        '-ss', str(seek_time),  # Seek to the specific time
        '-i', audio_url,
        '-f', 's16le',
        '-ac', '2',
        '-ar', '48000',
        '-'
    ]
    
    # Start ffmpeg process
    return subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=10**6)

def stream_audio(audio_url, seek_time=0):
    global process
    
    # Initialize PyAudio
    CHUNK = 1024
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=2,
                    rate=48000,
                    output=True)

    q = queue.Queue()
    
    # Start ffmpeg process with initial seek time
    process = start_ffmpeg_process(audio_url, seek_time)

    def read_ffmpeg_output():
        try:
            while True:
                chunk = process.stdout.read(CHUNK)
                if not chunk:
                    break
                q.put(chunk)
            q.put(None)
        finally:
            process.terminate()
            process.wait()

    threading.Thread(target=read_ffmpeg_output, daemon=True).start()

    try:
        while True:
            chunk = q.get()
            if chunk is None:
                break
            stream.write(chunk)
    except KeyboardInterrupt:
        pass
    finally:
        # Clean up
        stream.stop_stream()
        stream.close()
        p.terminate()

def seek_to_time(new_time, audio_url):
    global process
    if process:
        process.terminate()
        process.wait()
    stream_audio(audio_url, new_time)

try:
    audio_url = get_audio_url(video_link)
    print(f'Audio URL: {audio_url}')
    threading.Thread(target=stream_audio, args=(audio_url,), daemon=True).start()
    
    # Example to change time after 10 seconds
    time.sleep(5)  # Let the music play for 10 seconds
    print('Seeking to 50 seconds...')
    seek_to_time(50, audio_url)
    
except Exception as e:
    print(f"Error: {e}")
