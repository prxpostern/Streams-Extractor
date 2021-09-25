#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import filters
from pyrogram import Client as trojanz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyromod import listen

from config import Config
from script import Script

global tgtitle

@trojanz.on_message(filters.private & (filters.document | filters.video))
async def confirm_dwnld(client, message):

    if message.from_user.id not in Config.AUTH_USERS:
        return

    media = message
    filetype = media.document or media.video
    filename = filetype.file_name
    mes1 = await client.reply_text("<code>{filename}</code>")
    
    title = await client.ask(message.chat.id,'Enter Title :', filters=filters.text)
    tgtitle = title.text

    if filetype.mime_type.startswith("video/"):
        await message.reply_text(
            "**What you want me to do??**",
            quote=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text="DOWNLOAD and PROCESS", callback_data="download_file")],
                [InlineKeyboardButton(text="CANCEL", callback_data="close")]
            ])
        )
    else:
        await message.reply_text(
            "**What you want me to do??**",
            quote=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text="DOWNLOAD and PROCESS", callback_data="download_file")],
                [InlineKeyboardButton(text="CANCEL", callback_data="close")]
            ])
        )
    #else:
    #    await message.reply_text(
    #        "Invalid Media",
    #        quote=True
    #    )
