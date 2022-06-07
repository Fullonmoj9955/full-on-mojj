import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Diva1bot.events import register
from Diva1bot import telethn as tbot


PHOTO = "https://telegra.ph/file/914822a4e04ae926eaf08.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Diva.** \n\n"
    TEXT += "⚪ **I'm alive** \n\n"
    TEXT += f"⚪ **Managed By : [<✘𝗼 ✘𝗼 | 𝗔𝘃𝗶𝗶>](https://t.me/itz_xoxo)** \n\n"
    TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
    TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Thanku  🖤**"
    BUTTON = [

           



    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
