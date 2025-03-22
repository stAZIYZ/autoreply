import random
import asyncio
from telethon import TelegramClient, events
from dotenv import load_dotenv
import os


load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME")
channel_username = -1002460046152

comments = [
    "Zo'r post! 🚀",
    "Foydali ma'lumot! 👌",
    "Rahmat! 😍",
    "Juda qiziq post! 🌟",
    "Bu haqida oldin bilmagan edim! 😳"
]

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    post_id = event.message.id
    comment = random.choice(comments)
    await client.send_message(channel_username, comment, comment_to=post_id)
    print(f"Komment yozildi: {comment}")

async def main():
    await client.start()
    print("Bot ishlayapti...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
