import pyaudio
import yt_dlp
import subprocess
import threading
import queue

# Link of the video to be processed
video_link = "https://www.youtube.com/watch?v=S3Dpfyc15qQ"

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

def stream_audio(audio_url):
    # Prepare ffmpeg command
    ffmpeg_command = [
    'ffmpeg',
    '-loglevel', 'error',  # Adjust logging level to error to reduce verbose output
    '-i', audio_url,
    '-f', 's16le',
    '-ac', '2',
    '-ar', '48000',
    '-'
]

    
    # Start ffmpeg process
    process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=10**6)
    
    # Initialize PyAudio
    CHUNK = 1024
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=2,
                    rate=48000,
                    output=True)

    q = queue.Queue()

    def read_ffmpeg_output():
        try:
            while True:
                chunk = process.stdout.read(CHUNK)
                print(len(chunk))
                q.put(chunk)
                if not chunk:
                    break
            q.put(None)
            print('DONEEEEEEEEEEEEEEEEEE')
        finally:
            process.terminate()
            process.wait()  # Ensure the ffmpeg process has fully terminated

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

try:
    audio_url = get_audio_url(video_link)
    print(f'Audio URL: {audio_url}')
    stream_audio(audio_url)
except Exception as e:
    print(f"Error: {e}")