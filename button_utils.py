from telebot import types

mining_sovets = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
mining_sovets.add(types.KeyboardButton('Что такое майнинг?'),
                  types.KeyboardButton('Что такое трейдинг?'),
                  types.KeyboardButton('Стратегии трейдинга'),
                  types.KeyboardButton('Советы для трейдинга'),
                  types.KeyboardButton('Меню'))
