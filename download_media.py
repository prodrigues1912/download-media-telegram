import os

from telethon import TelegramClient, sync
from tqdm import tqdm

import settings as stg

client = TelegramClient("sessao_teste", stg.api_id, stg.api_hash)
client.start()

messages = client.get_messages(stg.telegram_group, limit=20000)
for msg in tqdm(messages):
    msg.download_media(file=os.path.join("media", stg.path))
