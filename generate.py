from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 29117903 
api_hash = "40da3cbc8a0db7acbc23d6f9a3b7cfb4" 

with TelegramClient(StringSession(), api_id, api_hash) as client:
    session_str = client.session.save()  
    print("Sizning string session: ", session_str)  
