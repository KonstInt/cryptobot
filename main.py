import telebot
import strings
import functions
import button_utils
from telebot import types
from py_currency_converter import convert
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()



bot = telebot.TeleBot("6260207697:AAHKctNDE5iT9o5AXJaOQO6mtSRuhg5hYOY")



@bot.message_handler(commands=['start'])
def adim(message):
    knopki = types.ReplyKeyboardMarkup(resize_keyboard=True)
    knopka1 = types.KeyboardButton('Курс криптовалют')
    knopka2 = types.KeyboardButton('Основы майнинга')
    knopka3 = types.KeyboardButton('Курс валют')
    knopki.row(knopka1, knopka2, knopka3)
    vib = bot.send_message(message.chat.id, 'Выберите опцию', reply_markup=knopki)
    bot.register_next_step_handler(vib, rasp)

def rasp(message):
    if message.text == 'Курс криптовалют':
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = types.KeyboardButton('RUB')
        knopka2 = types.KeyboardButton('USD')
        knopka3 = types.KeyboardButton('EUR')
        knopka = types.KeyboardButton('CNY')
        knopka4 = types.KeyboardButton('Меню')
        knopki.add(knopka1, knopka2, knopka3, knopka, knopka4)
        cr = bot.send_message(message.chat.id, 'Во что конвертировать?', reply_markup=knopki)
        bot.register_next_step_handler(cr, crypto)
    elif message.text == "Основы майнинга":
        osn = bot.send_message(message.chat.id, 'Что Вас интересует?', reply_markup=button_utils.mining_sovets)
        bot.register_next_step_handler(osn, mine)
    elif message.text == "/close":
        adem(message)
    elif message.text == "Курс валют":
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "RUB"
        knopka2 = "USD"
        knopka3 = "EUR"
        knopka4 = "CNY"
        knopka5 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5)
        k = bot.send_message(message.chat.id, "Какую валюту Вы хотите конвертировать?", reply_markup=knopki)
        bot.register_next_step_handler(k, kurs)
        
k1 = "adim"
k2 = "adim"       
def kurs(message):
    global k1
    global k2
    knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    knopka1 = "RUB"
    knopka2 = "USD"
    knopka3 = "EUR"
    knopka4 = "CNY"
    knopka5 = "Меню"
    knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5)
    if message.text == "RUB":
        k1 = "RUB"
        k2 = "₽"
    elif message.text == "USD":
        k1 = "USD"
        k2 = "$"
    elif message.text == "EUR":
        k1 = "EUR"
        k2 = "€"
    elif message.text == "CNY":
        k1 = "CNY"
        k2 = "¥"
    elif message.text == "Меню":
        adim(message)
        return
    elif message.text == "/close":
        adem(message)
        return
    k = bot.send_message(message.chat.id, "Во что конвертировать?", reply_markup=knopki)
    bot.register_next_step_handler(k, kurs2)
k32 = "adim"
def kurs2(message):
    global k32
    knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    knopka1 = "RUB"
    knopka2 = "USD"
    knopka3 = "EUR"
    knopka4 = "CNY"
    knopka5 = "Меню"
    knopkaBack = "Выбор конвертируемой валюты"
    knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5)
    if message.text == "RUB":
        k32 = "RUB"
        price = convert(base = k1, amount = 1, to=['RUB'])
        bot.send_message(message.chat.id, f'1{k2} = {price["RUB"]} ₽')
    elif message.text == "USD":
        k32 = "USD"
        price = convert(base = k1, amount = 1, to=['USD'])
        bot.send_message(message.chat.id, f'1{k2} = {price["USD"]} $')
    elif message.text == "EUR":
        k32 = "EUR"
        price = convert(base = k1, amount = 1, to=['EUR'])
        bot.send_message(message.chat.id, f'1{k2} = {price["EUR"]} €')
    elif message.text == "CNY":
        k32 = "CNY"
        price = convert(base = k1, amount = 1, to=['CNY'])
        bot.send_message(message.chat.id, f'1{k2} = {price["CNY"]} ¥')
        
    elif message.text == "Выбор конвертируемой валюты":
        k = bot.send_message(message.chat.id, "Какую валюту Вы хотите конвертировать?", reply_markup=(knopki))
        bot.register_next_step_handler(k, kurs)
        return
    elif message.text == "Меню":
        adim(message)
        return
    k = bot.send_message(message.chat.id, "Во что конвертировать?", reply_markup=knopki.add(knopkaBack))
    bot.register_next_step_handler(k, kurs2)


def crypto(message):
    knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    knopka1 = types.KeyboardButton('RUB')
    knopka2 = types.KeyboardButton('USD')
    knopka3 = types.KeyboardButton('EUR')
    knopka = types.KeyboardButton('CNY')
    knopka4 = types.KeyboardButton('Меню')
    knopki.add(knopka1, knopka2, knopka3, knopka, knopka4)
    
    if message.text == 'Меню':
        adim(message)
        return
    elif message.text == "/close":
        adem(message)
        return
    
    bot.send_message(message.chat.id, functions.cryptoStr(message.text.lower()))   
    cr = bot.send_message(message.chat.id, 'Во что конвертировать?', reply_markup=knopki)
    bot.register_next_step_handler(cr, crypto)
    
def mine(message):
    buttons = button_utils.mining_sovets
    if message.text == 'Меню':
        adim(message)
        return
    elif message.text == "/close":
        adem(message)
        return
    m = bot.send_message(message.chat.id, strings.sovets[message.text], reply_markup=buttons)
    bot.register_next_step_handler(m, mine)    
    
def adem(message):
    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'ок', reply_markup=a)
    
bot.infinity_polling()