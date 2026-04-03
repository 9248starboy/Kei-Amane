# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import asyncio, logging
from flask import Flask
from threading import Thread
from config import Config
from pyrogram import Client as VJ, idle
from typing import Union, Optional, AsyncGenerator
from plugins.regix import restart_forwards

# 🔥 Flask App (PORT FIX)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running ✅"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 🔥 Logging (optional)
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    VJBot = VJ(
        "VJ-Forward-Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        plugins=dict(root="plugins")
    )

    # 🔥 iter_messages (same as your code)
    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:

        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return

            messages = await self.get_messages(
                chat_id,
                list(range(current, current + new_diff + 1))
            )

            for message in messages:
                yield message
                current += 1

    # 🔥 Main Bot Function
    async def main():
        await VJBot.start()
        bot_info = await VJBot.get_me()
        logging.info(f"Bot Started as @{bot_info.username}")

        await restart_forwards(VJBot)

        print("✅ Bot Running Successfully...")
        await idle()

    # 🔥 Run Flask + Bot Together
    keep_alive()
    asyncio.get_event_loop().run_until_complete(main())
