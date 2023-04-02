from telebot import types

mining_sovets = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
mining_sovets.add(types.KeyboardButton('Что такое майнинг?'),
                  types.KeyboardButton('Что такое трейдинг?'),
                  types.KeyboardButton('Стратегии трейдинга'),
                  types.KeyboardButton('Советы для трейдинга'),
                  types.KeyboardButton('Меню'))
valute = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
valute.add(types.KeyboardButton('RUB'), types.KeyboardButton('USD'),
           types.KeyboardButton('EUR'), types.KeyboardButton('CNY'),
           types.KeyboardButton('Меню'))
