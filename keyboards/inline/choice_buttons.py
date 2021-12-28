from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import buy_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Купить апельсин 🍊",
                                          callback_data=buy_callback.new(item_name="apel",
                                                                         quantity=1)
                                      ),
                                      InlineKeyboardButton(
                                          text="Купить яблоко 🍏",
                                          callback_data=buy_callback.new(item_name="apple",
                                                                         quantity=1)
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Отмена",
                                          callback_data="cancel"
                                      )
                                  ]
                              ])
#Апельсин
apel_keyboard = InlineKeyboardMarkup()

APEL_LINK = "https://market.yandex.ru/product--apelsiny/1448825317?text=цена%20апельсина%201%20шт&cpc=LwFP4iXuJrtDSLufR_AKZZ1JAK5oQqhAeJ9sUOm03AzlRFcPRuM-YfAEUkMnUkqcJu5csOT6AYs6LvyYCPdplCl-9Jx1COmrAzCqQHZdutLOlAtCuuxN-DaT33TRIRmZ8kRj-zqLxVPgqSy-6GZCthZqEmfo3dByAqCv0G1UKgUItJejrMRREz8H9ipgkD9i&sku=101461003372&do-waremd5=kt1ERc13bHFzMhoCNNB3Kw&cpa=1&nid=55889"

apel_link = InlineKeyboardButton(text="Купи тут", url=APEL_LINK)

apel_keyboard.insert(apel_link)
#Яблоко
apple_keyboard = InlineKeyboardMarkup()

APPLE_LINK = "https://market.yandex.ru/product--iabloki-antonovka/1448847518?text=яблоки%20цена&cpc=ZF2LgGVOeADeribzAHmrbT3T5gxLXItGpvxWaOJRhxp7F8r6siTx8xgjQqtGXmRavE3eLLuYcHnjH7aqzm0X1o8D1hl_w_hw6ojkEoXOG9qtj2PSxQFhuyd5zYhlaayOkzvWTbmiQikMVtLD-nmpO8AIVwUVmUdBZumZi4YgRy6ZCObI47OBNL6pv7YtdNV3&sku=101460983552&do-waremd5=yq6hZiKTiyJQKGIDSsEA0g&cpa=1&nid=55889"

apple_link = InlineKeyboardButton(text="Купи тут", url=APPLE_LINK)

apple_keyboard.insert(apple_link)