import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import aiohttp

API_TOKEN = 'API_TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def fetch_messages():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://web:8000/api/v1/messages/') as response:
            return await response.json()


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm your bot!\nPowered by aiogram.")


@dp.message(Command("messages"))
async def list_messages(message: types.Message):
    messages = await fetch_messages()
    for msg in messages:
        await message.reply(f"Author: {msg['author']}\nMessage: {msg['text']}")


@dp.message(Command("new"))
async def create_new_message(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://web:8000/api/v1/message/', json={"author": message.from_user.username, "text": message.text.replace('/new ', '')}) as response:
            await message.reply("Message created!" if response.status == 200 else "Failed to create message.")

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())