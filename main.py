import telebot
import strings
import copy
import functions
import button_utils
import requests
from functions import trades_find_ask
from telebot import types
import requests
from py_currency_converter import convert
from pycoingecko import CoinGeckoAPI
from telebot import types
import json

cg = CoinGeckoAPI()


bot = telebot.TeleBot("6260207697:AAHKctNDE5iT9o5AXJaOQO6mtSRuhg5hYOY")


@bot.message_handler(commands=['start'])
def adim(message):
    knopki = types.ReplyKeyboardMarkup(resize_keyboard=True)
    knopka1 = types.KeyboardButton('Курс криптовалют')
    knopka2 = types.KeyboardButton('Основы майнинга')
    knopka3 = types.KeyboardButton('Курс валют')
<<<<<<< HEAD
    knopka4 = types.KeyboardButton('Данные с биржи')
=======
    knopka4 = types.KeyboardButton('Выбор видеокарты')
>>>>>>> 5d46c2b381e330c30ab6bae2a062fdf4027ffb63
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
<<<<<<< HEAD
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
=======

    elif message.text == "Выбор видеокарты":
        v = bot.send_message(message.chat.id,
                             'Чтобы найти оптимальную видеокарту для майнинга криптовалюты, введи бюджет (число) и название монеты, которую хочешь майнить. Например: "200 amd"".',
                             reply_markup=button_utils.videocart)

        bot.register_next_step_handler(message, find_best_graphics_card_message)


k1 = "adim"
k2 = "adim"

>>>>>>> 5d46c2b381e330c30ab6bae2a062fdf4027ffb63

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


URL = "https://min-api.cryptocompare.com/data/mining/equipment/general?api_key=5b8c2279cc108781bfca41f6aa2c8ea3ff842fae08e4eeb1b7fe73a338e7a6eb"

response = requests.get(URL)
data_all_cards = response.json()


def filter_graphics_cards(all_cards, coin, min_price=0, max_price=float("inf")):
    filtered_cards = []
    for card in all_cards:
        if coin and all_cards[card]["CurrenciesAvailable"].lower() != coin.lower():
            continue
        if float(all_cards[card]["Cost"]) < min_price or float(all_cards[card]["Cost"]) > max_price:
            continue
        filtered_cards.append(card)
    return filtered_cards


def find_best_graphics_card(budget, coin):
    cards = filter_graphics_cards(data_all_cards["Data"], coin)

    if not cards:
        return None

    all_cards = data_all_cards["Data"]

    best_card = None
    best_hashrate = 0
    for card in cards:
        hashrate = int(all_cards[card]["HashesPerSecond"])
        if hashrate > best_hashrate and float(all_cards[card]["Cost"]) <= budget:
            best_card = card
            best_hashrate = hashrate
    return best_card

@bot.message_handler(func=lambda message: True)
def find_best_graphics_card_message(message):
    text = message.text.lower()
    if message.text == 'Меню':
        adim(message)
        return
    elif " " not in text:
        bot.send_message(message.chat.id,
                         "Некорректный ввод. Введи бюджет (число) и название монеты, которую хочешь майнить. Например: '200 amd'.")
        return

    budget, coin = text.split(" ", 1)
    try:
        budget = int(budget)
    except ValueError:
        bot.send_message(message.chat.id,
                         "Некорректный ввод. Введи бюджет (число) и название монеты, которую хочешь майнить. Например: '200 amd'.")
        return

    card = find_best_graphics_card(budget, coin)
    if not card:
        bot.send_message(message.chat.id, "К сожалению, не удалось найти подходящую видеокарту.")
        return

    bot.send_message(message.chat.id,
                     f"Оптимальная видеокарта для майнинга {data_all_cards['Data'][card]['CurrenciesAvailableName']} с бюджетом {budget} USD: \n\n {data_all_cards['Data'][card]['Name']}\n {data_all_cards['Data'][card]['AffiliateURL']}")


bot.infinity_polling()
