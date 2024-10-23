# https://python-sounddevice.readthedocs.io/en/0.3.14/examples.html
import subprocess
import threading
import numpy as np
import queue
import sounddevice as sd
import sys
from contextlib import contextmanager
import time

# Queue to hold audio chunks
chunk_buffer = queue.Queue(maxsize=20)  # Adjust maxsize as needed

# Define the callback function for sounddevice
def callback(outdata, frames, time, status):
    if status.output_underflow:
        print('Output underflow: increase blocksize?', file=sys.stderr)
        raise sd.CallbackAbort
    try:
        chunk = chunk_buffer.get()
        if chunk is None:  # End of stream
            print('FINISBISISBSUSGHB')
            raise sd.CallbackStop
        #print("Chunk retrieved from buffer, size now:", chunk_buffer.qsize())
        data = np.frombuffer(chunk, dtype=np.int16)
        #data = np.clip(data * 0.1, -32768, 32767).astype(np.int16)
        data = data.reshape(-1, 2)
        # Check the length of the data
        n = data.shape[0]  # Number of samples in the chunk
        if n < frames:  # If there are fewer samples than frames
            print('111111111111111111111')
            outdata[:n] = data  # Fill available data
            outdata[n:] = 0  # Fill the rest with zeros
        else:  # If there are enough or more samples than frames
            outdata[:] = data[:frames]  # Fill the output buffer with data
    except queue.Empty:
        outdata[:] = 0  # Output silence if the buffer is empty

# Context manager to handle subprocess
@contextmanager
def managed_subprocess(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        yield process
        print('OIOIOIOIO')
    finally:
        print('AOAOAOAOA')
        process.stdout.close()
        process.stderr.close()
        process.terminate()
        process.wait()

# FFmpeg command to stream audio
track = {
    'url': 'https://rr1---sn-5hnekn7l.googlevideo.com/videoplayback?expire=1729659648&ei=oC4YZ_LqMfjQ6dsPi4HAkAo&ip=185.21.61.87&id=o-APwmEC6nsFxJaw66wautCRAvllEJ32QJW7sFQDoDreny&itag=251&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1729638048%2C&mh=UL&mm=31%2C29&mn=sn-5hnekn7l%2Csn-5hne6nz6&ms=au%2Crdu&mv=m&mvi=1&pl=22&rms=au%2Cau&initcwndbps=752500&vprv=1&svpuc=1&mime=audio%2Fwebm&rqh=1&gir=yes&clen=3883517&dur=233.321&lmt=1728042512257767&mt=1729637596&fvip=2&keepalive=yes&fexp=51312688%2C51326932&c=IOS&txp=5532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIgUoIPaBtIDiMGx38tvHDOIm8IN5y0gM-ew9OpITYQFZQCIQClaNt2ifSwDmmiYFJW5swldR774uIU2YIgzUytzGZ1fw%3D%3D&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=ACJ0pHgwRQIgN_RjAF3jXv-FXFxb9qmUACz3-d9kO3HfSg55GDrJQO8CIQCkK8yFF_6LutLlYyjr3Ts8-LnjMw8Cg09hrH9PWVwGkA%3D%3D'
    #'url': 'https://rr4---sn-5hnekn7l.googlevideo.com/videoplayback?expire=1729674248&ei=qGcYZ-TLLuTp6dsPy6jumQ4&ip=185.21.61.87&id=o-ABkXxyJckKrs9YtWJqF5mMS1VdGznzrX2NSKL5Edo5_8&itag=251&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1729652648%2C&mh=V-&mm=31%2C26&mn=sn-5hnekn7l%2Csn-4g5edn6r&ms=au%2Conr&mv=m&mvi=4&pl=22&rms=au%2Cau&initcwndbps=1037500&vprv=1&svpuc=1&mime=audio%2Fwebm&rqh=1&gir=yes&clen=160571&dur=10.061&lmt=1714545080019596&mt=1729652253&fvip=5&keepalive=yes&fexp=51312688%2C51326932&c=IOS&txp=8218224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRAIgKDjSxSz2pOBlYizNRDT6nW27vXM0MvlxeNU8Jrtsn_sCIH25lDNhjobwTosx7NZLnkiVXgG5A_kMUzSNJt-gYVQK&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=ACJ0pHgwRgIhAPlsW_it4pgtosXp5S3LgKBejfsg4HI1ZB06YKqpaJITAiEAzfh327S3-0YKQBNs_aP7Ugbx5zVfVKGWVb6BBsbnmXU%3D'
}

ffmpeg_command = [
    'ffmpeg',
    '-loglevel', 'error',
    '-i', track['url'],
    '-f', 's16le',
    '-ac', '2',  # Number of channels
    '-ar', '48000',  # Sample rate
    '-'  # Output to stdout
]

# Start the sounddevice stream
stream = sd.OutputStream(samplerate=48000, blocksize=int(1024),
                         channels=2, dtype='int16',)
                         #callback=callback)

stream.start()


# Thread to read FFmpeg output
def read_ffmpeg_output():
    with managed_subprocess(ffmpeg_command) as process:
        while True:
            chunk = process.stdout.read(1024)
            if not chunk:
                break
            chunk_buffer.put(chunk)
        print(chunk)
        print('bbbbbbbbbbbbbbbbbb')
        chunk_buffer.put(None)  # Signal end of stream

# Start the FFmpeg thread
ffmpeg_thread = threading.Thread(target=read_ffmpeg_output, daemon=True)
ffmpeg_thread.start()


try:
    while True:
        chunk = chunk_buffer.get()
        data = np.frombuffer(chunk, dtype=np.int16)
        data = data.reshape(-1, 2)
        stream.write(data)
except KeyboardInterrupt:
    print('Interrupted by user')
finally:
    # Stop the stream and wait for threads to finish
    stream.stop()
    stream.close()
    ffmpeg_thread.join()
    print('Playback finished')
