import telebot
import strings
import copy
import functions
import button_utils
from telebot import types
import requests
from py_currency_converter import convert
from pycoingecko import CoinGeckoAPI
from telebot import types
import json
import re

cg = CoinGeckoAPI()


bot = telebot.TeleBot("6154137866:AAF3p5BCuevuqWyD1QJmvN3jnqvetfr6vbQ")


@bot.message_handler(commands=['start'])
def adim(message):
    knopki = types.ReplyKeyboardMarkup(resize_keyboard=True)
    knopka1 = types.KeyboardButton('Курс криптовалют')
    knopka2 = types.KeyboardButton('Основы майнинга')
    knopka3 = types.KeyboardButton('Курс валют')
    knopka4 = types.KeyboardButton('Выбор видеокарты')
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

    elif message.text == "Выбор видеокарты":
        v = bot.send_message(message.chat.id,
                             'Чтобы найти оптимальную видеокарту для майнинга криптовалюты, введи бюджет (число) и название монеты, которую хочешь майнить. Например: "200 amd"".',
                             reply_markup=button_utils.videocart)

        bot.register_next_step_handler(message, find_best_graphics_card_message)


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
                         "Некорректный ввод. Введи бюджет (число), который планируешь потратить на покупку одной видеокарты, и название монеты, которую хочешь майнить. Например: '200 bitcoin'.")
        return

    budget, coin = text.split(" ", 1)
    try:
        budget = int(budget)
    except ValueError:
        bot.send_message(message.chat.id,
                         "Некорректный ввод. Введи бюджет (число), который планируешь потратить на покупку одной видеокарты, и название монеты, которую хочешь майнить. Например: '200 bitcoin'.")
        return

    crypto_currencies = {
        'btc': ['биткоин', 'btc', 'bitcoin', 'биток'],
        'ethw': ['эфириум', 'eth', 'ethereum', 'эфир'],
        'ltc': ['лайткоин', 'ltc', 'litecoin'],
        'doge': ['джеккоин', 'doge', 'dogecoin'],
    }

    coin_for_search = coin

    for currency, names in crypto_currencies.items():
        for name in names:
            if name in coin:
                coin_for_search = currency

    card = find_best_graphics_card(budget, coin_for_search)
    if not card:
        bot.send_message(message.chat.id, "К сожалению, не удалось найти подходящую видеокарту.")
        return

    bot.send_message(message.chat.id,
                     f"Оптимальная видеокарта для майнинга {data_all_cards['Data'][card]['CurrenciesAvailableName']} с бюджетом {budget} USD: \n\n {data_all_cards['Data'][card]['Name']}\n {data_all_cards['Data'][card]['AffiliateURL']}")


bot.infinity_polling()
