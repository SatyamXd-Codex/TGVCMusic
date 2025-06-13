from pyrogram import filters
from pyrogram.types import Message
from main import bot, vc
from helpers.yt import get_audio
import os

@bot.on_message(filters.command("play") & filters.group)
async def play_command(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Song name not provided.")
    
    query = " ".join(message.command[1:])
    await message.reply("🔍 Searching YouTube...")
    file_path = get_audio(query)
    
    if not file_path or not os.path.exists(file_path):
        return await message.reply("❌ Failed to get audio.")
    
    await vc.join_group_call(
        message.chat.id,
        file_path,
        stream_type="local"
    )
    await message.reply(f"▶️ Now Playing: **{query}**")
