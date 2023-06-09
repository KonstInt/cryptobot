from telebot import types

mining_sovets = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
mining_sovets.add(types.KeyboardButton('Меню'))
valute = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
valute.add(types.KeyboardButton('RUB'), types.KeyboardButton('USD'),
           types.KeyboardButton('EUR'), types.KeyboardButton('CNY'),
           types.KeyboardButton('Меню'))
videocart = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
videocart.add(types.KeyboardButton('Меню'))

news = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
news.add(types.KeyboardButton('Получить новость'), types.KeyboardButton('Меню'))

menu_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
menu_buttons.add(types.KeyboardButton('Курс криптовалют'),
        types.KeyboardButton('Основы майнинга'),
        types.KeyboardButton('Курс валют'),
        types.KeyboardButton('Данные с биржи'),
        types.KeyboardButton('Выбор видеокарты'),
        types.KeyboardButton('Новости'))
buttons_exchange = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
buttons_exchange.add(types.KeyboardButton('Сумма проданных монет'),
        types.KeyboardButton('Сумма купленных монет'),
        types.KeyboardButton('Общая сумма выставленных на закуп монет'),
        types.KeyboardButton('Меню'))
buttons_crypto = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
buttons_crypto.add(types.KeyboardButton('btc'),
        types.KeyboardButton('eth'),
        types.KeyboardButton('ltc'),
        types.KeyboardButton('usdt'),
        types.KeyboardButton('Назад'),
        types.KeyboardButton('Меню'))
