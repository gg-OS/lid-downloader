import customtkinter as ctk
import threading
import time
from pathlib import Path
import os
from downloader import yt_downloader
from playlist_catcher import playlist_lister
from bitrate_enhancer import enhancer
from safe_download import safe_download

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MainMenuFrame(ctk.CTkFrame):
    """Main menu with navigation buttons"""
    
    def __init__(self, parent, show_single_callback, show_playlist_callback):
        super().__init__(parent)
        self.show_single_callback = show_single_callback
        self.show_playlist_callback = show_playlist_callback
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = ctk.CTkLabel(self, text="LID Downloader 🎵", font=ctk.CTkFont(size=32, weight="bold"))
        title.pack(pady=40)
        
        # Single song button
        single_btn = ctk.CTkButton(
            self, 
            text="Download a single song 🎵",
            font=ctk.CTkFont(size=16),
            height=50,
            width=300,
            command=self.show_single_callback
        )
        single_btn.pack(pady=20)
        
        # Playlist button
        playlist_btn = ctk.CTkButton(
            self,
            text="Download a playlist 📜", 
            font=ctk.CTkFont(size=16),
            height=50,
            width=300,
            command=self.show_playlist_callback
        )
        playlist_btn.pack(pady=20)

class SingleDownloadFrame(ctk.CTkFrame):
    """Single song download interface"""
    
    def __init__(self, parent, return_callback):
        super().__init__(parent)
        self.return_callback = return_callback
        self.is_downloading = False
        self.music_folder = Path.home() / "Music"
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = ctk.CTkLabel(self, text="Download Single Song", font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=20)
        
        # URL input
        url_label = ctk.CTkLabel(self, text="YouTube URL:")
        url_label.pack(pady=(20, 5))
        
        self.url_entry = ctk.CTkEntry(self, width=400, placeholder_text="https://youtube.com/watch?v=...")
        self.url_entry.pack(pady=5)
        
        # Download button
        self.download_btn = ctk.CTkButton(
            self,
            text="Start Download",
            height=40,
            command=self.start_download
        )
        self.download_btn.pack(pady=20)
        
        # Progress bar
        self.progress = ctk.CTkProgressBar(self, width=400)
        self.progress.pack(pady=10)
        self.progress.set(0)
        
        # Status label
        self.status_label = ctk.CTkLabel(self, text="Ready to download")
        self.status_label.pack(pady=10)
        
        # Return button
        return_btn = ctk.CTkButton(
            self,
            text="Return to Main Menu",
            command=self.return_callback
        )
        return_btn.pack(pady=20)
    
    def start_download(self):
        if self.is_downloading:
            return
            
        url = self.url_entry.get().strip()
        if not url:
            self.status_label.configure(text="Please enter a YouTube URL")
            return
        
        self.is_downloading = True
        self.download_btn.configure(state="disabled")
        self.progress.set(0)
        
        # Start download simulation in background thread
        thread = threading.Thread(target=self.simulate_download)
        thread.daemon = True
        thread.start()
    
    def simulate_download(self):
        """Actually download the song"""
        url = self.url_entry.get().strip()
        
        try:
            # Ensure music folder exists
            os.makedirs(self.music_folder, exist_ok=True)
            
            # Step 1: Download
            self.status_label.configure(text="Downloading audio...")
            self.progress.set(0.3)
            filename = yt_downloader(url, str(self.music_folder))
            
            # Step 2: Try to enhance quality (skip if ffmpeg not available)
            self.status_label.configure(text="Enhancing quality...")
            self.progress.set(0.7)
            try:
                original_file = self.music_folder / f"{filename}.mp3"
                temp_enhanced = self.music_folder / f"{filename}_enhanced.mp3"
                enhancer(str(original_file), str(temp_enhanced))
            except Exception:
                # Skip enhancement if ffmpeg not available
                pass
            
            # Step 3: Complete
            self.progress.set(1.0)
            self.status_label.configure(text=f"✅ Download complete! The file was saved in {self.music_folder}.")
            
        except Exception as e:
            self.status_label.configure(text=f"❌ Error: {str(e)}")
            self.progress.set(0)
        
        finally:
            self.download_btn.configure(state="normal")
            self.is_downloading = False

class PlaylistDownloadFrame(ctk.CTkFrame):
    """Playlist download interface"""
    
    def __init__(self, parent, return_callback):
        super().__init__(parent)
        self.return_callback = return_callback
        self.is_downloading = False
        self.music_folder = Path.home() / "Music"
        self.playlist_urls = []
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = ctk.CTkLabel(self, text="Download Playlist", font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=20)
        
        # URL input
        url_label = ctk.CTkLabel(self, text="Playlist URL:")
        url_label.pack(pady=(20, 5))
        
        self.url_entry = ctk.CTkEntry(self, width=400, placeholder_text="https://youtube.com/playlist?list=...")
        self.url_entry.pack(pady=5)
        
        # List playlist button
        list_btn = ctk.CTkButton(
            self,
            text="List Playlist Items",
            command=self.list_playlist
        )
        list_btn.pack(pady=10)
        
        # Playlist items display
        self.playlist_text = ctk.CTkTextbox(self, width=500, height=150)
        self.playlist_text.pack(pady=10)
        
        # Download button
        self.download_btn = ctk.CTkButton(
            self,
            text="Start Download",
            height=40,
            command=self.start_download
        )
        self.download_btn.pack(pady=20)
        
        # Progress bar
        self.progress = ctk.CTkProgressBar(self, width=400)
        self.progress.pack(pady=10)
        self.progress.set(0)
        
        # Status label
        self.status_label = ctk.CTkLabel(self, text="Ready to download")
        self.status_label.pack(pady=10)
        
        # Return button
        return_btn = ctk.CTkButton(
            self,
            text="Return to Main Menu",
            command=self.return_callback
        )
        return_btn.pack(pady=20)
    
    def list_playlist(self):
        """Actually list playlist items"""
        url = self.url_entry.get().strip()
        if not url:
            self.playlist_text.delete("0.0", "end")
            self.playlist_text.insert("0.0", "Please enter a playlist URL first")
            return
        
        try:
            self.status_label.configure(text="Loading playlist...")
            self.playlist_urls = playlist_lister(url)
            
            # Display playlist items
            playlist_display = "\n".join([f"{i+1}. {url}" for i, url in enumerate(self.playlist_urls)])
            self.playlist_text.delete("0.0", "end")
            self.playlist_text.insert("0.0", playlist_display)
            self.status_label.configure(text=f"Playlist loaded ({len(self.playlist_urls)} items)")
            
        except Exception as e:
            self.playlist_text.delete("0.0", "end")
            self.playlist_text.insert("0.0", f"Error loading playlist: {str(e)}")
            self.status_label.configure(text="Failed to load playlist")
    
    def start_download(self):
        if self.is_downloading:
            return
            
        playlist_content = self.playlist_text.get("0.0", "end").strip()
        if not playlist_content or "Please enter" in playlist_content:
            self.status_label.configure(text="Please list playlist items first")
            return
        
        self.is_downloading = True
        self.download_btn.configure(state="disabled")
        self.progress.set(0)
        
        # Start download simulation in background thread
        thread = threading.Thread(target=self.simulate_playlist_download)
        thread.daemon = True
        thread.start()
    
    def simulate_playlist_download(self):
        """Actually download playlist"""
        if not hasattr(self, 'playlist_urls') or not self.playlist_urls:
            self.status_label.configure(text="Please list playlist items first")
            self.download_btn.configure(state="normal")
            self.is_downloading = False
            return
        
        try:
            # Ensure music folder exists
            os.makedirs(self.music_folder, exist_ok=True)
            
            total_songs = len(self.playlist_urls)
            
            for i, url in enumerate(self.playlist_urls):
                self.status_label.configure(text=f"Downloading song {i+1}/{total_songs}...")
                
                # Download with error handling
                safe_download(url, str(self.music_folder))
                
                # Update progress
                progress = (i + 1) / total_songs
                self.progress.set(progress)
            
            # Complete
            self.status_label.configure(text=f"✅ All songs downloaded! Files saved in {self.music_folder}.")
            
        except Exception as e:
            self.status_label.configure(text=f"❌ Error: {str(e)}")
            self.progress.set(0)
        
        finally:
            self.download_btn.configure(state="normal")
            self.is_downloading = False

class App(ctk.CTk):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("LID Downloader")
        self.geometry("600x700")
        self.resizable(False, False)
        
        # Initialize frames
        self.main_menu = MainMenuFrame(self, self.show_single_download, self.show_playlist_download)
        self.single_download = SingleDownloadFrame(self, self.show_main_menu)
        self.playlist_download = PlaylistDownloadFrame(self, self.show_main_menu)
        
        # Show main menu initially
        self.show_main_menu()
    
    def hide_all_frames(self):
        """Hide all frames"""
        for frame in [self.main_menu, self.single_download, self.playlist_download]:
            frame.pack_forget()
    
    def show_main_menu(self):
        """Show main menu"""
        self.hide_all_frames()
        self.main_menu.pack(fill="both", expand=True, padx=20, pady=20)
    
    def show_single_download(self):
        """Show single download screen"""
        self.hide_all_frames()
        self.single_download.pack(fill="both", expand=True, padx=20, pady=20)
    
    def show_playlist_download(self):
        """Show playlist download screen"""
        self.hide_all_frames()
        self.playlist_download.pack(fill="both", expand=True, padx=20, pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()