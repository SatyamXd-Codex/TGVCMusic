# 🎧 TGVC Music Bot

**TGVC Music** is a simple and stable Telegram music bot for streaming high-quality audio in group voice chats.  
Built using **Pyrogram**, **PyTgCalls**, and **yt-dlp** — without MongoDB, clean and easy to deploy.

---

## 🚀 Features

- 🎵 Play music directly from YouTube in Telegram voice chats
- 🎚 Simple commands: `/play`, `/pause`, `/resume`, `/stop`
- 👑 `/broadcast` command for sudo users (send message to all groups)
- ⚡ Lightweight and fast — no MongoDB or heavy setup required
- 🛠 Easy to configure with a single `config.py` file

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/SatyamXd-Codex/TGVCMusic
cd TGVCMusic
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Fill in your config

Edit the `config.py` file:

```python
API_ID = 123456
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"
SESSION_STRING = "your_session_string"
SUDO_USERS = [123456789, 987654321]  # Your Telegram User IDs
```

> 🔐 You can generate `SESSION_STRING` using [Pyrogram String Session Generator](https://docs.pyrogram.org/topics/sessions#string-session)

### 4. Run the bot

```bash
python3 main.py
```

---

## 💬 Bot Commands

| Command        | Description                          |
|----------------|--------------------------------------|
| `/play <name>` | Play a song in group voice chat      |
| `/pause`       | Pause the current stream             |
| `/resume`      | Resume paused stream                 |
| `/stop`        | Leave voice chat and stop playback   |
| `/broadcast`   | (Sudo Only) Send message to all chats|

---

## 📂 Folder Structure

```
tgvc_music/
├── main.py
├── config.py
├── requirements.txt
├── helpers/
│   └── yt.py
├── plugins/
│   ├── play.py
│   ├── controls.py
│   └── broadcast.py
```

---

## 📋 Requirements

- Python 3.9 or higher
- Telegram API credentials from [my.telegram.org](https://my.telegram.org)
- A Telegram Bot from [@BotFather](https://t.me/BotFather)

---

## 👑 Credits

- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Bot made with ❤️ By [Hexor'Xd](https://t.me/Sher_E_Purvanchal)

---

## 📜 License

This project is open-source and free to use under the Apache License.
