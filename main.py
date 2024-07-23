import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards import keyboard
from aiogram.enums import ChatType

from database import Database

TOKEN = "6832038787:AAHxvFRzHgKwrYfoPnDC-wjitGFkD6rzguQ"


dp = Dispatcher()

db = Database("db.db")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        text=f"Assalomu alaykum <b><i>{message.from_user.first_name}</i></b>!\n\nBotimizga hush kelibsiz!",
        parse_mode='html',
        reply_markup=keyboard)


@dp.message(F.chat.type.in_({"group", "supergroup"}))
async def add_user(message: Message):
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

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())