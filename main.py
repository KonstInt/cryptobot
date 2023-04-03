import telebot
import strings
import copy
import functions
import button_utils
import requests
from functions import trades_find_ask
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
    knopka4 = types.KeyboardButton('Данные с биржи')
    knopki.row(knopka1, knopka2, knopka3, knopka4)
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
    elif message.text == 'Данные с биржи':
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        knopka1 = "Сумма проданных монет"
        knopka2 = "Сумма купленных монет"
        knopka3 = "Общая сумма выставленных на закуп монет"
        knopka4 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4)
        bir = bot.send_message(message.chat.id, "Какая информация вам интересна?", reply_markup=knopki)
        bot.register_next_step_handler(bir, exchange)
k1 = "adim"
k2 = "adim"

def exchange(message):
    if (message.text == "Общая сумма выставленных на закуп монет"):
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "btc"
        knopka2 = "eth"
        knopka3 = "ltc"
        knopka4 = "usdt"
        knopka5 = "Назад"
        knopka6 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5, knopka6)
        ex = bot.send_message(message.chat.id, f"Выберите валюту для подсчёта", reply_markup=knopki)
        bot.register_next_step_handler(ex, exchange_sum)
    elif (message.text == "Меню"):
        adim(message)
    elif (message.text == "Сумма проданных монет"):
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "btc"
        knopka2 = "eth"
        knopka3 = "ltc"
        knopka4 = "usdt"
        knopka5 = "Назад"
        knopka6 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5, knopka6)
        ex1 = bot.send_message(message.chat.id, f"Выберите валюту для подсчёта", reply_markup=knopki)
        bot.register_next_step_handler(ex1, exchange_ask)
    else:
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "btc"
        knopka2 = "eth"
        knopka3 = "ltc"
        knopka4 = "usdt"
        knopka5 = "Назад"
        knopka6 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5, knopka6)
        ex2 = bot.send_message(message.chat.id, f"Выберите валюту для подсчёта", reply_markup=knopki)
        bot.register_next_step_handler(ex2, exchange_bid)



def exchange_bid(message):
    if (message.text == "Назад"):
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        knopka1 = "Сумма проданных монет"
        knopka2 = "Сумма купленных монет"
        knopka3 = "Общая сумма выставленных на закуп монет"
        knopka4 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4)
        bir2 = bot.send_message(message.chat.id, "Какая информация вам интересна?", reply_markup=knopki)
        bot.register_next_step_handler(bir2, exchange)
    elif (message.text == "Меню"):
        adim(message)
    else:
        bot.send_message(message.chat.id, functions.trades_find_bid(coin1=message.text))
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "btc"
        knopka2 = "eth"
        knopka3 = "ltc"
        knopka4 = "usdt"
        knopka5 = "Назад"
        knopka6 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5, knopka6)
        ex_bid = bot.send_message(message.chat.id, "Выберите валюту", reply_markup=knopki)
        bot.register_next_step_handler(ex_bid, exchange_bid)


def exchange_ask(message):
    if (message.text == "Назад"):
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        knopka1 = "Сумма проданных монет"
        knopka2 = "Сумма купленных монет"
        knopka3 = "Общая сумма выставленных на закуп монет"
        knopka4 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4)
        bir2 = bot.send_message(message.chat.id, "Какая информация вам интересна?", reply_markup=knopki)
        bot.register_next_step_handler(bir2, exchange)
    elif (message.text == "Меню"):
        adim(message)
    else:
        bot.send_message(message.chat.id, functions.trades_find_ask(coin1=message.text))
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "btc"
        knopka2 = "eth"
        knopka3 = "ltc"
        knopka4 = "usdt"
        knopka5 = "Назад"
        knopka6 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5, knopka6)
        ex_ask = bot.send_message(message.chat.id, "Выберите валюту", reply_markup=knopki)
        bot.register_next_step_handler(ex_ask, exchange_ask)


def exchange_sum(message):
    if (message.text == "Назад"):
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        knopka1 = "Сумма проданных монет"
        knopka2 = "Сумма купленных монет"
        knopka3 = "Общая сумма выставленных на закуп монет"
        knopka4 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4)
        bir2 = bot.send_message(message.chat.id, "Какая информация вам интересна?", reply_markup=knopki)
        bot.register_next_step_handler(bir2, exchange)
    elif (message.text == "Меню"):
        adim(message)
    else:
        bot.send_message(message.chat.id, functions.depth_find(coin1 = message.text))
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "btc"
        knopka2 = "eth"
        knopka3 = "ltc"
        knopka4 = "usdt"
        knopka5 = "Назад"
        knopka6 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5, knopka6)
        ex2 = bot.send_message(message.chat.id, "Выберите валюту", reply_markup=knopki)
        bot.register_next_step_handler(ex2, exchange_sum)

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