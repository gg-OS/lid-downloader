from downloader import yt_downloader
from bitrate_enhancer import enhancer
from playlist_catcher import playlist_lister
from safe_download import safe_download
import os, time, random

folder = "downloaded"

if not os.path.exists(folder):
    os.makedirs(folder)



selected = input("Select 1 for video and 2 for playlist: ")

if selected == '1':  # Video

    video_url = "https://www.youtube.com/watch?v=BbxE_HTiKJg"

    # Download function
    base_filename = yt_downloader(video_url, folder)

    input_audio = os.path.join(folder, f"{base_filename}.mp3")
    output_audio = os.path.join(folder, f"{base_filename}_enhanced.mp3")

    # Enhancer function
    enhancer(input_audio, output_audio)

    print("Done!")

elif selected == '2':  # Playlist
    
    playlist_url = "https://www.youtube.com/playlist?list=PLW9NlkHMPoNlxCOSIK7ov-EAyc5L3MJNO"

    all_videos = playlist_lister(playlist_url)

    for item in all_videos:
        safe_download(item, folder)
        delay = random.randint(10, 40)
        time.sleep(delay)

else:
    print('Invalid selection.')

"""# Download function
base_filename = yt_downloader(video_url, folder)

input_audio = os.path.join(folder, f"{base_filename}.mp3")
output_audio = os.path.join(folder, f"{base_filename}_enhanced.mp3")

# Enhancer function
enhancer(input_audio, output_audio)

print("Done!")"""
