import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards import keyboard
from aiogram.enums import ChatType
from aiogram.types import User, Chat, ChatPermissions

from database import Database

TOKEN = "6832038787:AAHxvFRzHgKwrYfoPnDC-wjitGFkD6rzguQ"
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

db = Database("db.db")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        text=f"Assalomu alaykum <b><i>{message.from_user.first_name}</i></b>!\n\nBotimizga hush kelibsiz!",
        parse_mode='html',
        reply_markup=keyboard)


@dp.message(Command("top"), F.chat.type.in_({"group", "supergroup"}))
async def top(message: Message):
    top_user = db.get_top_user(message.chat.id)

    text = "-------------TOP USERS------------\n"
    
    for i in top_user:
        #print(i[3])
        chat: Chat = await bot.get_chat(chat_id=i[1])
        #print(chat.first_name)
        text += f"{chat.first_name}: {i[3]}\n"

    await message.answer(text=text)

@dp.message(F.chat.type.in_({"group", "supergroup"}))
async def add_user(message: Message):

    user_count = db.get_count(message.from_user.id, message.chat.id)
    if user_count <= 10:
        await message.delete()
        await message.answer(f"{message.from_user.full_name} guruhga 10 ta odam qo'shmaguningizcha yoza olmaysiz qo'shgan odamlaringiz soni {user_count}")

    new_members = message.new_chat_members
    if new_members is not None:
        for member in new_members:
            await message.answer(f"Assalomu alaykum <b>{member.first_name}!</b>\nSizni guruhga <b>{message.from_user.first_name}</b> qo'shdi")
            adder = message.from_user.id
            chat_id = message.chat.id
            db.update_count_user(adder, chat_id, 1)
    else:
        pass


async def main():

    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())