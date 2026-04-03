# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import sys
import asyncio 
from database import Db, db
from config import Config, temp
from script import Script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import psutil
import time as time
from os import environ, execle, system

START_TIME = time.time()

# 🔥 PREMIUM UI BUTTONS
main_buttons = [

    # Top Row (Developer - Center Feel)
    [
        InlineKeyboardButton('❣️ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 ❣️', url='https://t.me/kingvj01')
    ],

    # Row 2 (Equal Width Feel)
    [
        InlineKeyboardButton(' 🔍 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ', url='https://t.me/vj_bot_disscussion'),
        InlineKeyboardButton(' 🤖 𝗨𝗣𝗗𝗔𝗧𝗘 ', url='https://t.me/vj_botz')
    ],

    # Row 3
    [
        InlineKeyboardButton(' 👨‍💻 𝗛𝗘𝗟𝗣 ', callback_data='help'),
        InlineKeyboardButton(' 💁 𝗔𝗕𝗢𝗨𝗧 ', callback_data='about')
    ],

    # Bottom Row
    [
        InlineKeyboardButton('⚙️ 𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦', callback_data='settings#main')
    ]

]

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    user = message.from_user

    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, user.first_name)

    await client.send_message(
        chat_id=message.chat.id,
        text=Script.START_TXT.format(user.first_name),
        reply_markup=InlineKeyboardMarkup(main_buttons)
    )

@Client.on_message(filters.private & filters.command(['restart']) & filters.user(Config.BOT_OWNER))
async def restart(client, message):
    msg = await message.reply_text("<i>Restarting...</i>")
    await asyncio.sleep(3)
    await msg.edit("<i>Server restarted successfully ✅</i>")
    system("git pull -f && pip3 install --no-cache-dir -r requirements.txt")
    execle(sys.executable, sys.executable, "main.py", environ)

@Client.on_callback_query(filters.regex('help'))
async def helpcb(bot, query):
    buttons = [
        [InlineKeyboardButton('🤔 𝗛𝗢𝗪 𝗧𝗢 𝗨𝗦𝗘 ❓', callback_data='how_to_use')],
        [
            InlineKeyboardButton('✨ 𝗔𝗕𝗢𝗨𝗧', callback_data='about'),
            InlineKeyboardButton('⚙ 𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦', callback_data='settings#main')
        ],
        [InlineKeyboardButton('⬅ 𝗕𝗔𝗖𝗞', callback_data='back')]
    ]

    await query.message.edit_text(
        text=Script.HELP_TXT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex('how_to_use'))
async def how_to_use(bot, query):
    await query.message.edit_text(
        text=Script.HOW_USE_TXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⬅ 𝗕𝗔𝗖𝗞', callback_data='help')]]),
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex('back'))
async def back(bot, query):
    await query.message.edit_text(
        text=Script.START_TXT.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(main_buttons)
    )

@Client.on_callback_query(filters.regex('about'))
async def about(bot, query):
    buttons = [
        [
            InlineKeyboardButton('⬅ 𝗕𝗔𝗖𝗞', callback_data='help'),
            InlineKeyboardButton('📊 𝗦𝗧𝗔𝗧𝗦', callback_data='status')
        ]
    ]

    await query.message.edit_text(
        text=Script.ABOUT_TXT,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex('status'))
async def status(bot, query):
    users_count, bots_count = await db.total_users_bots_count()
    forwardings = await db.forwad_count()
    uptime = await get_bot_uptime(START_TIME)

    buttons = [
        [
            InlineKeyboardButton('⬅ 𝗕𝗔𝗖𝗞', callback_data='help'),
            InlineKeyboardButton('💻 𝗦𝗬𝗦𝗧𝗘𝗠', callback_data='systm_sts')
        ]
    ]

    await query.message.edit_text(
        text=Script.STATUS_TXT.format(uptime, users_count, bots_count, forwardings),
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex('systm_sts'))
async def system_status(bot, query):
    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent()
    disk = psutil.disk_usage('/')

    text = f"""
<b>💻 SERVER STATS</b>

💾 Total: {disk.total / (1024**3):.2f} GB
📦 Used: {disk.used / (1024**3):.2f} GB
🆓 Free: {disk.free / (1024**3):.2f} GB

⚙ CPU: {cpu}%
🧠 RAM: {ram}%
"""

    await query.message.edit_text(
        text=text,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⬅ 𝗕𝗔𝗖𝗞', callback_data='help')]])
    )

async def get_bot_uptime(start_time):
    seconds = int(time.time() - start_time)
    minutes = seconds // 60
    hours = minutes // 60
    return f"{hours%24}H {minutes%60}M {seconds%60}S"
