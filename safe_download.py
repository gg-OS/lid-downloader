import pytubefix
import time
from pathlib import Path
from downloader import yt_downloader
from bitrate_enhancer import enhancer

def safe_download(url, folder):
    try:
        filename = yt_downloader(url, folder)
        
        # Enhance audio quality
        try:
            folder_path = Path(folder)
            original_file = folder_path / f"{filename}.mp3"
            temp_enhanced = folder_path / f"{filename}_enhanced.mp3"
            enhancer(str(original_file), str(temp_enhanced))
        except Exception:
            # Skip enhancement if ffmpeg not available
            pass
            
    except pytubefix.exceptions.VideoUnavailable:
        print(f"Video {url} is unavailable. Skipping...")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        print("Retrying in 5 minutes...")
        time.sleep(300)  # Wait 5 minutes before retrying
