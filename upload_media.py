import os

from telethon import TelegramClient, sync

import settings as stg


client = TelegramClient("test_session", stg.api_id, stg.api_hash)
client.start()

for root, _, files in os.walk(stg.path):
    file_dictionary = {int(sub.split(".")[0]): sub for sub in files}
    for key, value in sorted(file_dictionary.items()):
        print(os.path.join(root, value))
        client.send_file(
            stg.telegram_group,
            file=os.path.join(root, value),
            caption=value[:-4],
            supports_streaming=True
        )

