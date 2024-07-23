from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, SwitchInlineQueryChosenChat

add_me = InlineKeyboardButton(
    text="Guruhga qo'shsish", 
    url="https://t.me/hisob_kitob_1307_bot?startgroup=true",
)
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [add_me],
    ]
)