from telethon import TelegramClient
import asyncio
import time
from telethon import events

api_id = '13046591'
api_hash = '4c78f2ac8ecf6d313102fd2ee8ae8a83'

client = TelegramClient('Username', api_id, api_hash)

message = 'Hey, I will be at a retreat until Saturday. I promise to get in touch as soon as I can. See you.'

def main():

    client.start()
    
    @client.on(events.NewMessage(incoming=True))
    async def _(event):
        if event.is_private:
            time.sleep(1)  # pause for 1 second to rate-limit automatic replies
            await client.send_message(event.message.from_id, message)
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
