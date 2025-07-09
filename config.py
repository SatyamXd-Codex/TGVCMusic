import os
import json
import sys
from dotenv import load_dotenv

class Config:
    CONFIG_FILE = "config.json"
    
    def __init__(self):
        # Try loading from config.json first
        self.config = {}
        try:
            if os.path.exists(self.CONFIG_FILE):
                with open(self.CONFIG_FILE, 'r') as f:
                    self.config = json.load(f)
        except Exception as e:
            print(f"Error loading config file: {e}")
        
        # Then try loading from environment variables
        load_dotenv()
        
        # Required values
        self.API_ID = self._get_config("api_id") or os.getenv("API_ID")
        self.API_HASH = self._get_config("api_hash") or os.getenv("API_HASH")
        self.BOT_TOKEN = self._get_config("bot_token") or os.getenv("BOT_TOKEN")
        self.SESSION_NAME = self._get_config("session_name") or os.getenv("SESSION_NAME") or "TGVCMusic"
        
        # Optional values with defaults
        self.ADMINS = self._parse_list(self._get_config("admins")) or self._parse_env_list("ADMINS") or ["me"]
        self.DOWNLOAD_PATH = self._get_config("download_path") or os.getenv("DOWNLOAD_PATH") or "downloads"
        self.DURATION_LIMIT = int(self._get_config("duration_limit") or os.getenv("DURATION_LIMIT") or "10")
        
        # MongoDB settings
        self.USE_MONGODB = self._parse_bool(self._get_config("use_mongodb") or os.getenv("USE_MONGODB") or "false")
        self.MONGODB_URI = self._get_config("mongodb_uri") or os.getenv("MONGODB_URI")
        
        # Validate required settings
        self._validate_config()
    
    def _get_config(self, key):
        return self.config.get(key)
    
    def _parse_list(self, value):
        if isinstance(value, list):
            return value
        return None
    
    def _parse_env_list(self, key):
        value = os.getenv(key)
        if value:
            return value.split(',')
        return None
    
    def _parse_bool(self, value):
        if isinstance(value, bool):
            return value
        return str(value).lower() in ('true', 'yes', 'y', '1')
    
    def _validate_config(self):
        missing = []
        
        if not self.API_ID:
            missing.append("API_ID")
        if not self.API_HASH:
            missing.append("API_HASH")
        if not self.BOT_TOKEN:
            missing.append("BOT_TOKEN")
        
        if self.USE_MONGODB and not self.MONGODB_URI:
            missing.append("MONGODB_URI (required when USE_MONGODB is enabled)")
        
        if missing:
            print("Error: Missing required configuration values:")
            for item in missing:
                print(f" - {item}")
            print("\nPlease run 'python setup.py' to configure the application.")
            sys.exit(1)

# Create a global instance for easy importing
config = Config()