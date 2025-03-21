from pytubefix import YouTube
from pytubefix.cli import on_progress
from bitrate_enhancer import enhancer
import os

video_url = "https://www.youtube.com/watch?v=BbxE_HTiKJg"

folder = "downloaded"

if not os.path.exists(folder):
    os.makedirs(folder)

yt = YouTube(video_url, on_progress_callback=on_progress)
print(f"Video title: {yt.title}")

base_filename = yt.title.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')

audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
audio_stream.download(output_path=folder, filename=f"{base_filename}.mp3")


input_audio = os.path.join(folder, f"{base_filename}.mp3")  # Original MP3
output_audio = os.path.join(folder, f"{base_filename}_enhanced.mp3")  # Enhanced MP3

enhancer(input_audio, output_audio)

print("Audio downloaded successfully as .mp3!")
