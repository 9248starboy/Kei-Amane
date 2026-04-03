Don't Remove Credit Tg - @VJ_Botz

import asyncio
from flask import Flask
from pyrogram import Client as VJ
from config import Config
from plugins.regix import restart_forwards

------------------ FLASK ------------------

app = Flask(name)

@app.route("/")
def home():
return "Bot is running ✅"

------------------ BOT ------------------

VJBot = VJ(
"VJ-Forward-Bot",
bot_token=Config.BOT_TOKEN,
api_id=Config.API_ID,
api_hash=Config.API_HASH,
sleep_threshold=120,
plugins=dict(root="plugins")
)

async def main():
await VJBot.start()
await restart_forwards(VJBot)
print("Bot Started Successfully 🚀")

# keep alive WITHOUT idle()
await asyncio.Event().wait()

------------------ MAIN ------------------

if name == "main":
loop = asyncio.get_event_loop()

# run bot in background task (NOT thread)
loop.create_task(main())

# run flask normally
app.run(host="0.0.0.0", port=10000)
