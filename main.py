import os
import sys
import logging
from pyrogram import Client, idle
from config import config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Check if config exists, if not, guide user to run setup.py
if not os.path.exists("config.json") and not os.getenv("API_ID"):
    logger.info("Configuration not found. Please run 'python setup.py' first.")
    logger.info("Alternatively, set the required environment variables.")
    sys.exit(1)

def main():
    # Initialize the bot client
    plugins = dict(root="plugins")
    app = Client(
        config.SESSION_NAME,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        bot_token=config.BOT_TOKEN,
        plugins=plugins
    )

    # Create download directory if not exists
    if not os.path.isdir(config.DOWNLOAD_PATH):
        os.makedirs(config.DOWNLOAD_PATH)

    # Start the bot
    logger.info("Starting TGVCMusic Bot...")
    app.start()
    logger.info("Bot started successfully!")
    
    # Idle to keep the bot running
    idle()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user!")
    except Exception as e:
        logger.error(f"Bot encountered an error: {e}")
    finally:
        logger.info("Exiting...")
        sys.exit(0)