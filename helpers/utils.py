import os
import asyncio
from typing import Union
from pyrogram.types import Message
from config import config

# Check if user is admin
def is_admin(user_id: Union[str, int]) -> bool:
    if not config.ADMINS:
        return False
    
    if str(user_id) in config.ADMINS:
        return True
    
    if "me" in config.ADMINS:
        return True  # Everyone is admin if "me" is in admins list
    
    return False

# Convert seconds to readable time
def format_duration(seconds: int) -> str:
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    if hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    else:
        return f"{minutes}m {seconds}s"

# Clean downloaded files
async def clean_downloads():
    try:
        for file in os.listdir(config.DOWNLOAD_PATH):
            filepath = os.path.join(config.DOWNLOAD_PATH, file)
            try:
                if os.path.isfile(filepath) and not filepath.endswith('.gitignore'):
                    os.remove(filepath)
            except Exception as e:
                print(f"Error deleting {filepath}: {e}")
    except Exception as e:
        print(f"Error cleaning downloads folder: {e}")