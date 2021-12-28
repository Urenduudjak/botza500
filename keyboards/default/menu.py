from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1")
        ],
        [
            KeyboardButton(text="2"),
            KeyboardButton(text="3")
        ],
    ],
    resize_keyboard=True
)