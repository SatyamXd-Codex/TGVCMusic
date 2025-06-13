from pyrogram import filters
from pyrogram.types import Message
from main import bot, vc

@bot.on_message(filters.command("pause") & filters.group)
async def pause(_, message: Message):
    await vc.pause_stream(message.chat.id)
    await message.reply("⏸️ Paused.")

@bot.on_message(filters.command("resume") & filters.group)
async def resume(_, message: Message):
    await vc.resume_stream(message.chat.id)
    await message.reply("▶️ Resumed.")

@bot.on_message(filters.command("stop") & filters.group)
async def stop(_, message: Message):
    await vc.leave_group_call(message.chat.id)
    await message.reply("⏹️ Stopped and Left VC.")
