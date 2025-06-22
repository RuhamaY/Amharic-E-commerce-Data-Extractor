from telethon.sync import TelegramClient
import json
from dotenv import load_dotenv
import os


load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone = os.getenv("PHONE")

client = TelegramClient('session_name', api_id, api_hash)

channel_usernames = [
    'ZemenExpress',
    'nevacomputer',
    'helloomarketethiopia',
    'Fashiontera',
    'kuruwear'
]

async def scrape_messages():
    await client.start(phone)
    all_data = []

    for channel in channel_usernames:
        try:
            async for message in client.iter_messages(channel, limit=100):
                if message.text:
                    data = {
                        "channel": channel,
                        "date": str(message.date),
                        "text": message.text,
                        "views": message.views or 0,
                        "id": message.id,
                        "image_url": str(message.media) if message.media else None
                    }
                    all_data.append(data)
        except Exception as e:
            print(f"Failed to read from {channel}: {e}")

    with open("raw_telegram_data.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

with client:
    client.loop.run_until_complete(scrape_messages())
