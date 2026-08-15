# LID Downloader - User Guide 🎵

## What is this?

LID Downloader is a simple desktop app that lets you download music from YouTube as high-quality MP3 files.

---

## How to Get Started

### Option 1: Download the Ready-to-Use App (Recommended)

1. **Download** the `LID_Downloader.zip` file
2. **Extract** the ZIP file to a folder (like your Desktop or Documents)
3. **Double-click** `LID_Downloader.exe` to run the app
4. That's it! No installation needed.

### Option 2: Run from Source (For Advanced Users)

If you have Python installed:
1. Open Command Prompt in the app folder
2. Type: `pip install -r requirements_gui.txt`
3. Type: `python gui_mockup.py`

---

## How to Use

### Downloading a Single Song

1. **Open the app** - You'll see the main menu
2. **Click** "Download a single song 🎵"
3. **Copy** a YouTube video URL (like: `https://youtube.com/watch?v=...`)
4. **Paste** it into the URL box
5. **Click** "Check URL" - The song title will appear
6. **Click** "Start Download" - Wait for it to finish
7. **Done!** Your song is saved in your Music folder

**Want to download another?** Click "Download Another Song" button.

### Downloading a Playlist

1. **Click** "Download a playlist 📜" from the main menu
2. **Copy** a YouTube playlist URL (like: `https://youtube.com/playlist?list=...`)
3. **Paste** it into the URL box
4. **Click** "List Playlist Items" - You'll see all songs
5. **Click** "Start Download" - The app will download all songs
6. **Be patient** - The app waits 10-40 seconds between songs to avoid being blocked by YouTube

### Changing Where Files Are Saved

By default, songs are saved to your **Music** folder.

To change this:
1. Look for the "Output:" section at the bottom
2. Click the **"Change"** button
3. Select a folder where you want your music saved
4. The app will remember your choice for next time

---

## Understanding the App

### What You'll See

- **Progress Bar**: Shows download progress
- **Status Messages**: Tells you what's happening
  - "Downloading audio..." - Getting the song from YouTube
  - "Enhancing quality..." - Improving audio quality to 320kbps
  - "✅ Download complete!" - Your song is ready
  - "❌ Error..." - Something went wrong (see troubleshooting below)

### Audio Quality

- Songs are downloaded in **320kbps MP3** format (very high quality)
- This requires FFmpeg (included in the download package)
- If FFmpeg is missing, songs download at standard quality

---

## Troubleshooting

### "The app won't open"

- Make sure you extracted the ZIP file (don't run from inside the ZIP)
- Try right-click → "Run as Administrator"
- Check if Windows Defender blocked it (click "More info" → "Run anyway")

### "Download failed" or "Error" message

- **Check your internet connection**
- **Try a different video** - Some videos are restricted or unavailable
- **Wait a few minutes** - YouTube might have temporarily blocked you
- **Copy the URL again** - Make sure it's correct

### "Video unavailable"

- The video might be private, deleted, or region-restricted
- Try a different video

### "Can't find my downloaded songs"

- Check your **Music** folder (usually `C:\Users\YourName\Music`)
- Or check the folder shown in "Output:" at the bottom of the app
- Click "Change" to pick a different folder

### Playlist downloads are slow

- This is normal! The app waits 10-40 seconds between songs
- This prevents YouTube from blocking you
- Large playlists can take a while - be patient

### "Enhancing quality" takes forever

- This step improves audio quality to 320kbps
- It can take 10-30 seconds per song
- If FFmpeg is missing, this step is skipped automatically

---

## Tips & Tricks

✅ **Use playlists** - Download multiple songs at once instead of one by one

✅ **Let it run** - You can minimize the app while it downloads

✅ **Check the title** - Always verify the song title before downloading

✅ **Organize your music** - Use the "Change" button to save to different folders for different artists/genres

✅ **Be patient with playlists** - The delays are there to protect you from being blocked

❌ **Don't close the app** while downloading - You'll lose progress

❌ **Don't download too many playlists** in a row - Take breaks to avoid YouTube rate limits

---

## Legal Notice

⚠️ **Important**: This tool is for personal use only.

- Only download music you have the right to download
- Respect copyright laws in your country
- Don't distribute downloaded files
- Support artists by buying their music when possible

---

## Need More Help?

If you're still having issues:

1. **Check the console window** (if visible) for detailed error messages
2. **Try restarting the app**
3. **Make sure YouTube works in your browser** first
4. **Check if the video/playlist is public** and accessible

---

## Quick Reference

| Task | Steps |
|------|-------|
| Download 1 song | Main Menu → Single Song → Paste URL → Check URL → Download |
| Download playlist | Main Menu → Playlist → Paste URL → List Items → Download |
| Change save location | Click "Change" button next to "Output:" |
| Download another | Click "Download Another Song" button |
| Go back | Click "Return to Main Menu" |

---

**Enjoy your music! 🎵**
