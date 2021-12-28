import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_data import buy_callback
from keyboards.inline.choice_buttons import choice, apel_keyboard, apple_keyboard
from loader import dp


@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text="На продажу апельсин и яблоко. \n"
                              "Если вам ничего не нужно - жмите отмену",
                         reply_markup=choice)


@dp.callback_query_handler(text_contains="apel")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Вы выбрали купить апельсин.\n"
                              "Спасибо)",
                              reply_markup=apel_keyboard)


@dp.callback_query_handler(text_contains="apple")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Вы выбрали купить яблоко.\n"
                              "Спасибо)",
                              reply_markup=apple_keyboard)


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("Вы отменили эту покупку!", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)