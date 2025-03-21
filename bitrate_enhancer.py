import subprocess, os

def enhancer(audio_file, audio_path):

    command = f'ffmpeg -i "{audio_file}" -b:a 192K -vn "{audio_path}"'
    subprocess.run(command, shell=True)

    if os.path.exists(audio_file):
        os.remove(audio_file)


    final_audio_path = audio_file
    os.rename(audio_path, final_audio_path)
    print(f"Renamed {audio_path} to {final_audio_path}")
