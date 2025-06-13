from pyrogram import filters
from pyrogram.types import Message
from config import SUDO_USERS
from main import bot

@bot.on_message(filters.command("broadcast") & filters.user(SUDO_USERS))
async def broadcast(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Message required for broadcast.")
    
    broadcast_text = "📢 Broadcast:\n" + " ".join(message.command[1:])
    success, failed = 0, 0

    async for dialog in bot.iter_dialogs():
        try:
            await bot.send_message(dialog.chat.id, broadcast_text)
            success += 1
        except:
            failed += 1
    
    await message.reply(f"✅ Sent to {success} chats\n❌ Failed in {failed} chats")
