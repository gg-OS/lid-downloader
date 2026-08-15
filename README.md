# LID Downloader 🎵

A portable desktop application for downloading YouTube audio in high quality with a modern GUI interface.

## Features

- **Single Song Download**: Download individual YouTube videos as high-quality audio
- **Playlist Download**: Download entire YouTube playlists with anti-bot detection delays
- **Audio Enhancement**: Automatic bitrate improvement to 320kbps using FFmpeg
- **Portable**: No external dependencies required when properly configured
- **Modern GUI**: Clean, dark-themed interface built with CustomTkinter
- **Folder Selection**: Choose custom download location
- **Settings Persistence**: Remembers your preferences

## Quick Start

### Run GUI (Development)
```bash
pip install -r requirements_gui.txt
python gui_mockup.py
```

### Run CLI (Legacy)
```bash
python main.py
```

### Build Windows Executable
```bash
pip install pyinstaller
pyinstaller lid_downloader.spec
```
Executable will be in `dist/LID_Downloader/LID_Downloader.exe`

## Installation & Setup

### 1. Install Python Dependencies
```bash
pip install -r requirements_gui.txt
```

### 2. Setup FFmpeg (Optional but Recommended)
1. Download FFmpeg from https://ffmpeg.org/download.html
2. Extract `ffmpeg.exe` from the bin/ folder
3. Place it in the `ffmpeg/` folder in this project
4. Audio enhancement will be automatically enabled

### 3. Run the Application
```bash
python gui_mockup.py
```

## Project Structure

```
lid-downloader/
├── gui_mockup.py          # Main GUI application
├── downloader.py          # YouTube video downloader
├── playlist_catcher.py    # Playlist URL extractor
├── bitrate_enhancer.py    # Audio quality enhancer
├── safe_download.py       # Download with error handling
├── main.py               # Legacy CLI (deprecated)
├── ffmpeg/               # Local FFmpeg executable folder
│   ├── ffmpeg.exe       # Place FFmpeg here
│   └── README.txt       # Setup instructions
└── requirements_gui.txt  # Python dependencies
```

## Module Functions

### `downloader.py`
- **`yt_downloader(video_url, folder)`**: Downloads YouTube video as MP3 audio file
- Handles filename sanitization and selects highest quality audio stream

### `playlist_catcher.py`
- **`playlist_lister(playlist_url)`**: Extracts all video URLs from a YouTube playlist
- Returns list of individual video URLs for batch processing

### `bitrate_enhancer.py`
- **`enhancer(audio_file, audio_path)`**: Enhances audio bitrate to 320K using FFmpeg with libmp3lame codec
- Uses local FFmpeg executable for portability
- Automatically replaces original file with enhanced version

### `safe_download.py`
- **`safe_download(url, folder)`**: Downloads with error handling and retry logic
- Handles video unavailability and network errors
- Implements 5-minute retry delay for failed downloads

### `gui_mockup.py`
- **Main Application**: Modern GUI interface with three screens
- **Anti-Bot Protection**: Random 10-40 second delays between playlist downloads
- **Progress Tracking**: Real-time download progress and status updates
- **Error Handling**: User-friendly error messages and recovery

## Usage

### Single Song Download
1. Launch the application
2. Click "Download a single song 🎵"
3. Paste YouTube video URL
4. Click "Start Download"
5. Audio file will be saved to your Music folder

### Playlist Download
1. Click "Download a playlist 📜"
2. Paste YouTube playlist URL
3. Click "List Playlist Items" to preview
4. Click "Start Download"
5. All songs will be downloaded with anti-bot delays

## Anti-Bot Protection

The application includes built-in protection against YouTube's bot detection:
- Random delays (10-40 seconds) between playlist downloads
- Error handling for rate limiting
- Retry logic with extended delays

## File Locations

- **Downloads**: Default is your system's Music folder, customizable via GUI
- **Enhanced Audio**: Original files are replaced with 320K bitrate versions
- **Settings**: Stored in `~/.lid_downloader_config.json`
- **Logs**: Console output shows download progress and any errors

## Building for Distribution

### Windows Executable

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Build using spec file:
```bash
pyinstaller lid_downloader.spec
```

3. Find executable in:
```
dist/LID_Downloader/LID_Downloader.exe
```

4. **Important**: Place `ffmpeg.exe` in the `ffmpeg/` folder before building, or include it in the distribution package.

### Distribution Package Structure
```
LID_Downloader/
├── LID_Downloader.exe
├── ffmpeg/
│   └── ffmpeg.exe
└── [other DLLs and dependencies]
```

## Troubleshooting

### FFmpeg Not Found
- Ensure `ffmpeg.exe` is placed in the `ffmpeg/` folder
- Audio will download without enhancement if FFmpeg is missing
- Download FFmpeg from: https://ffmpeg.org/download.html

### Download Errors
- Check internet connection
- Verify YouTube URL is valid and accessible
- Some videos may be region-restricted or unavailable
- Try waiting a few minutes if rate-limited

### GUI Not Responding
- Downloads run in background threads
- Large playlists may take time due to anti-bot delays (10-40s between songs)
- Check console output for detailed progress

### Build Issues
- Ensure all dependencies are installed: `pip install -r requirements_gui.txt`
- Use the provided spec file: `pyinstaller lid_downloader.spec`
- If missing modules, add to `hiddenimports` in spec file

### Settings Not Saving
- Check write permissions in home directory
- Settings file location: `~/.lid_downloader_config.json`
- Delete settings file to reset to defaults

## Dependencies

- `customtkinter>=5.2.0` - Modern GUI framework
- `pytubefix` - YouTube download functionality
- `ffmpeg.exe` - Audio enhancement (optional)

## License

This tool is for personal use only. Respect YouTube's Terms of Service and copyright laws.