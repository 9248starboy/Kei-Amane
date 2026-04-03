# Don't Remove Credit Tg - @VJ_Botz

import asyncio
import threading
from flask import Flask
from pyrogram import Client as VJ, idle
from config import Config
from plugins.regix import restart_forwards

# ------------------ FLASK ------------------

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running ✅"

# ------------------ BOT ------------------

def run_bot():
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
        await idle()

    asyncio.run(main())

# ------------------ MAIN ------------------

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
