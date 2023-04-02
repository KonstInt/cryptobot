import telebot
import strings
import copy
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
    knopki = button_utils.valute
    
    if message.text == "Меню":
        adim(message)
        return
    elif message.text == "/close":
        adem(message)
        return
    k1 = message.text
    k = bot.send_message(message.chat.id, "Во что конвертировать?", reply_markup=knopki)
    bot.register_next_step_handler(k, kurs2)

def kurs2(message):
    knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    knopka1 = "RUB"
    knopka2 = "USD"
    knopka3 = "EUR"
    knopka4 = "CNY"
    knopka5 = "Меню"
    knopkaBack = "Выбор конвертируемой валюты"
    knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5)
    if message.text == "Выбор конвертируемой валюты":
        k = bot.send_message(message.chat.id, "Какую валюту Вы хотите конвертировать?", reply_markup=(knopki))
        bot.register_next_step_handler(k, kurs)
        return
    elif message.text == "Меню":
        adim(message)
        return
    bot.send_message(message.chat.id, functions.valuteStr(k1, message.text))
    k = bot.send_message(message.chat.id, "Во что конвертировать?", reply_markup=(knopki).add(knopkaBack))
    bot.register_next_step_handler(k, kurs2)


def crypto(message):
    
    if message.text == 'Меню':
        adim(message)
        return
    elif message.text == "/close":
        adem(message)
        return
    
    bot.send_message(message.chat.id, functions.cryptoStr(message.text.lower()))   
    cr = bot.send_message(message.chat.id, 'Во что конвертировать?', reply_markup=button_utils.valute)
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