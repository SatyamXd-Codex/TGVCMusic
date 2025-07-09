# TGVCMusic Bot

A Telegram Voice Chat Music Bot to play music in voice chats with many features.

## Features

- Play music from YouTube
- Play music from local files
- Queue system
- Control playback (pause, resume, skip)
- Admin commands
- Docker support for easy deployment

## Quick Setup Guide

### Method 1: Standard Setup

1. Clone the repository
   ```bash
   git clone https://github.com/SatyamXd-Codex/TGVCMusic
   cd TGVCMusic
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run setup script to configure bot
   ```bash
   python setup.py
   ```

4. Start the bot
   ```bash
   python main.py
   ```

### Method 2: Docker Setup

1. Clone the repository
   ```bash
   git clone https://github.com/SatyamXd-Codex/TGVCMusic
   cd TGVCMusic
   ```

2. Build and run with Docker Compose
   ```bash
   docker-compose up -d
   ```

   The bot will automatically run the setup script if no configuration is found.

## Environment Variables

If you prefer not to use the setup script, you can set these environment variables:

- `API_ID`: Your Telegram API ID
- `API_HASH`: Your Telegram API Hash
- `BOT_TOKEN`: Your Telegram Bot Token
- `SESSION_NAME`: Session name (default: TGVCMusic)
- `ADMINS`: Comma-separated list of admin usernames or IDs
- `USE_MONGODB`: Whether to use MongoDB (true/false)
- `MONGODB_URI`: MongoDB connection URI
- `DOWNLOAD_PATH`: Path to store downloaded songs
- `DURATION_LIMIT`: Max song duration in minutes

## Commands

- `/play [song name or YouTube URL]` - Play a song
- `/pause` - Pause the current playback
- `/resume` - Resume playback
- `/skip` - Skip the current song
- `/stop` - Stop playing and clear the queue
- `/queue` - Show the current queue
- `/help` - Show help message

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.