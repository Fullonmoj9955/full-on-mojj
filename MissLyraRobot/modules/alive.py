import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from MissLyraRobot.events import register
from MissLyraRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/290f2dd056aec4fd19c3e.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm FULLONMOJJ_BOT.** \n\n"
    TEXT += "⚪ **I'm alive** \n\n"
    TEXT += f"⚪ **Managed By : [<༒☬PANDIT ☬JI ༒>](https://t.me/Panditji097)** \n\n"
    TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
    TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Thanku  ✨🖤**"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/Diva1bot?start=help"),
            Button.url("ѕᴜᴘᴘᴏʀᴛ​", "https://t.me/panditji021"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT)
