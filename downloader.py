from pytubefix import YouTube
from pytubefix.cli import on_progress


def yt_downloader(video_url, folder):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    print(f"Video title: {yt.title}")

    base_filename = yt.title.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')

    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    audio_stream.download(output_path=folder, filename=f"{base_filename}.mp3")

    return base_filename