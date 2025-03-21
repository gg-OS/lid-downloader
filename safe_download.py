import pytubefix
import time
from downloader import yt_downloader

def safe_download(url, folder):
    try:
        yt_downloader(url, folder)
    except pytubefix.exceptions.VideoUnavailable:
        print(f"Video {url} is unavailable. Skipping...")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        print("Retrying in 5 minutes...")
        time.sleep(300)  # Wait 5 minutes before retrying
