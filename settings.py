import json
import os
from pathlib import Path

class Settings:
    """Manage application settings with JSON persistence"""
    
    def __init__(self):
        self.config_file = Path.home() / ".lid_downloader_config.json"
        self.defaults = {
            "output_folder": str(Path.home() / "Music"),
            "last_mode": "single"
        }
        self.data = self.load()
    
    def load(self):
        """Load settings from file or return defaults"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return {**self.defaults, **json.load(f)}
            except:
                return self.defaults.copy()
        return self.defaults.copy()
    
    def save(self):
        """Save current settings to file"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2)
        except:
            pass
    
    def get(self, key, default=None):
        """Get setting value"""
        return self.data.get(key, default)
    
    def set(self, key, value):
        """Set setting value and save"""
        self.data[key] = value
        self.save()
