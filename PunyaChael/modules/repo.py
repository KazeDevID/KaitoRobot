from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from PunyaChael import pbot, START_IMG, SUPPORT_CHAT


@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""✨ **Hey I'm ROBOT** 

**Developer : [Lord-Kaze](https://t.me/KenalSayaaa)**
**Python Version :** `{y()}`
**Library Version :** `{o}`
**Telethon Version :** `{s}`
**Pyrogram Version :** `{z}`

**Click on Button Bellow For More**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Source Code🕺", url=f"https://github.com/PunyaChael/KaitoRobot"), 
                    InlineKeyboardButton(
                        "SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}")
                ]
            ]
        )
    )
