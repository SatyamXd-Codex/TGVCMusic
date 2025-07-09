from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("help") & filters.group)
async def help_group(client, message: Message):
    await message.reply_text(
        "Click the button below to get help",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Help", url=f"https://t.me/{(await client.get_me()).username}?start=help")]
        ])
    )

@Client.on_message(filters.command("start") & filters.private)
async def start_private(client, message: Message):
    if len(message.command) > 1 and message.command[1] == "help":
        await help_private(client, message)
        return
        
    await message.reply_text(
        f"👋 Hello {message.from_user.mention}!\n\n" +
        "I am TGVCMusic Bot, a bot that can play music in voice chats.\n\n" +
        "Send /help to get more information."
    )

@Client.on_message(filters.command("help") & filters.private)
async def help_private(client, message: Message):
    await message.reply_text(
        "**TGVCMusic Bot Help**\n\n" +
        "**Basic Commands:**\n" +
        "/play [song name or YouTube URL] - Play a song or add to queue\n" +
        "/pause - Pause the current playback\n" +
        "/resume - Resume the paused playback\n" +
        "/skip - Skip the current song\n" +
        "/stop - Stop playing and clear the queue\n" +
        "/queue - Show the current queue\n\n" +
        "**Admin Commands:**\n" +
        "/reload - Reload the bot (Admin only)\n" +
        "/clean - Clean downloaded files (Admin only)\n\n" +
        "**Note:** The bot will only respond to admins for control commands."
    )