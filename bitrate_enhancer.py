import subprocess, os, sys

def get_ffmpeg_path():
    """Get path to local ffmpeg executable"""
    if getattr(sys, 'frozen', False):
        # Running as PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running as normal Python script
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    ffmpeg_path = os.path.join(base_path, 'ffmpeg', 'ffmpeg.exe')
    return ffmpeg_path

def enhancer(audio_file, audio_path):
    ffmpeg_exe = get_ffmpeg_path()
    
    if not os.path.exists(ffmpeg_exe):
        raise FileNotFoundError(f"FFmpeg not found at {ffmpeg_exe}. Please place ffmpeg.exe in the /ffmpeg folder.")
    
    command = f'"{ffmpeg_exe}" -i "{audio_file}" -b:a 192K -vn "{audio_path}"'
    subprocess.run(command, shell=True)

    if os.path.exists(audio_file):
        os.remove(audio_file)

    final_audio_path = audio_file
    os.rename(audio_path, final_audio_path)
    print(f"Renamed {audio_path} to {final_audio_path}")
