from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("start"))
async def show_menu(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! \n\n"
                         f"Выбирите кнопку", reply_markup=menu)


@dp.message_handler(text="1")
async def get_one(message: types.Message):
    await message.answer("Вы выбрали: 1")


@dp.message_handler(Text(equals=[2, 3]))
async def get_twothree(message: types.Message):
    await message.answer(f"Вы выбрали: {message.text}", reply_markup=ReplyKeyboardRemove())