from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_STRING
from plugins import play, controls, broadcast

bot = Client("TGVCBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client("TGVCUser", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
vc = PyTgCalls(user)

@bot.on_message(filters.command("start") & filters.private)
async def start(_, msg):
    await msg.reply("🎵 **TGVC Music Bot is Live!**\nUse `/play` in group voice chat to play music.")

def start_all():
    bot.start()
    user.start()
    vc.start()
    print("✅ TGVC Music Bot Started")
    import asyncio
    asyncio.get_event_loop().run_forever()

start_all()
