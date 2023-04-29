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
import search
cg = CoinGeckoAPI()


bot = telebot.TeleBot('')
current_function = ''

@bot.message_handler(commands=['start', 'close', 'help'])
def adim(message):
    knopki = button_utils.menu_buttons
    
    if message.text=='/close':
        adem(message)
    elif message.text == '/start':
        vib = bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}\nВыберите опцию ', reply_markup=knopki)
        bot.register_next_step_handler(vib, rasp)
    elif message.text == 'Меню':
        vib = bot.send_message(message.chat.id, f'Выберите опцию ', reply_markup=knopki)
        bot.register_next_step_handler(vib, rasp)
    elif message.text == '/help':
        bot.send_message(message.chat.id, strings.help_command)
        vib = bot.send_message(message.chat.id, f'Теперь выберите подходящую Вам опцию ', reply_markup=knopki)
        bot.register_next_step_handler(vib, rasp)
    else:
        vib = bot.send_message(message.chat.id, f'Я вас не понимаю...\nВыберите опцию нажав на кнопки ниже', reply_markup=knopki)
        bot.register_next_step_handler(vib, rasp)

# def help(message):
#     global current_function
#     bot.send_message(message.chat.id, strings.help_command)
#     current_function = ''
#     adim('/start')
#     return 

links = []
def rasp(message):
    global current_function
    global links
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
    elif message.text == '/help':
        adim(message)
        return
    elif message.text == "Курс валют":
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "RUB"
        knopka2 = "USD"
        knopka3 = "EUR"
        knopka4 = "CNY"
        knopka5 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5)
        current_function = 'Курс валют'
        bot.send_message(message.chat.id, "Какую валюту Вы хотите конвертировать?", reply_markup=knopki)
        #bot.register_next_step_handler(k, kurs)

    elif message.text == "Выбор видеокарты":
        
        current_function = message.text
        v = bot.send_message(message.chat.id,
                             'Чтобы найти оптимальную видеокарту для майнинга криптовалюты, введи бюджет (число) и название монеты, которую хочешь майнить. Например: "500 etc".',
                             reply_markup=button_utils.videocart)
        bot.register_next_step_handler(message, find_best_graphics_card_message)
    elif message.text == 'Данные с биржи':
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        knopka1 = "Сумма проданных монет"
        knopka2 = "Сумма купленных монет"
        knopka3 = "Общая сумма выставленных на закуп монет"
        knopka4 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4)
        bir = bot.send_message(message.chat.id, "Какая информация вам интересна?", reply_markup=knopki)
        bot.register_next_step_handler(bir, exchange)
    elif message.text == 'Новости':
        bot.send_message(message.chat.id, "Подождите, идёт загрузка новостей...")
        knopki = button_utils.news
        links = functions.get_links_news()
        current_function = 'Новости'
        bot.send_message(message.chat.id, 'Хотите получить свежую новость?', reply_markup = knopki)
    else:
        adim(message)

k1 = "adim"
k2 = "adim"
i = 0

@bot.message_handler(func = lambda x: current_function == 'Новости')
def get_news_1(message):
    global current_function
    
    if message.text == 'Получить новость':
        current_function = 'Новости 2'
        get_news_2(message)
        return
    elif message.text == 'Меню':
        current_function = ''
        adim(message)
        return
    elif message.text == '/help':
        adim(message)
        return
        # bot.send_message(message.chat.id, strings.help_command)
        # vib = bot.send_message(message.chat.id, f'Теперь выберите подходящую Вам опцию ', reply_markup=button_utils.menu_buttons)
        # bot.register_next_step_handler(vib, rasp)

@bot.message_handler(func = lambda x: current_function == 'Новости 2')
def get_news_2(message):
    global current_function
    global links
    global i
    bot.send_message(message.chat.id, links[i])
    i += 1
    if i >= len(links):
        i = 0
    knopki = button_utils.news
    bot.send_message(message.chat.id, 'Хотите получить ещё одну свежую новость?', reply_markup = knopki)
    current_function = 'Новости'

@bot.message_handler(func = lambda x: current_function == 'Курс валют')
def kurs(message):
    global k1
    global k2
    global current_function
    knopki = button_utils.valute

    if message.text == "Меню":
        current_function = ''
        adim(message)
        return
    elif message.text == '/help':
        adim(message)
        return
    k1 = message.text
    current_function = "Курс валют 2"
    bot.send_message(message.chat.id, "Во что конвертировать?", reply_markup=knopki)
    

@bot.message_handler(func = lambda x: current_function == 'Курс валют 2')
def kurs2(message):
    global current_function
    knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    knopka1 = "RUB"
    knopka2 = "USD"
    knopka3 = "EUR"
    knopka4 = "CNY"
    knopka5 = "Меню"
    knopkaBack = "Выбор конвертируемой валюты"
    knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5)
    if message.text == "Выбор конвертируемой валюты":
        current_function = 'Курс валют'
        bot.send_message(message.chat.id, "Какую валюту Вы хотите конвертировать?", reply_markup=(knopki))
        return
    elif message.text == "Меню":
        current_function = ''
        adim(message)
        return
    bot.send_message(message.chat.id, functions.valuteStr(k1, message.text))
    bot.send_message(message.chat.id, "Во что конвертировать?", reply_markup=(knopki).add(knopkaBack))
    


def crypto(message):
    if message.text == 'Меню':
        adim(message)
        return
    elif message.text == "/close":
        adem(message)
        return
    elif message.text == '/help':
        adim(message)
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
    elif message.text == '/help':
        adim(message)
        return
    rv = search.search_results(message.text)
    m = bot.send_message(message.chat.id, rv , reply_markup=buttons)
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

@bot.message_handler(func=lambda l: current_function=="Выбор видеокарты")
def find_best_graphics_card_message(message):
    text = message.text.lower()
    if message.text == 'Меню':
        global current_function
        current_function = ''
        adim(message)
        return
    elif message.text == '/help':
        adim(message)
        return
    elif " " not in text:
        bot.send_message(message.chat.id,
                         "Некорректный ввод. Введи бюджет (число) и название монеты, которую хочешь майнить. Например: '500 etc'.")
        return

    budget, coin = text.split(" ", 1)
    try:
        budget = int(budget)
    except ValueError:
        bot.send_message(message.chat.id,
                         "Некорректный ввод. Введи бюджет (число) и название монеты, которую хочешь майнить. Например: '500 etc'.")
        return

    card = find_best_graphics_card(budget, coin)
    if not card:
        bot.send_message(message.chat.id, "К сожалению, не удалось найти подходящую видеокарту.")
        return

    bot.send_message(message.chat.id,
                     f"Оптимальная видеокарта для майнинга {data_all_cards['Data'][card]['CurrenciesAvailableName']} с бюджетом {budget} USD: \n\n {data_all_cards['Data'][card]['Name']}\n {data_all_cards['Data'][card]['AffiliateURL']}")

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
    elif message.text == '/help':
        adim(message)
        return
    elif message.text == '/close':
        adem(message)
        return
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
    elif message.text == '/help':
        adim(message)
        return
    elif message.text == '/close':
        adem(message)
        return
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
    elif message.text == '/help':
        adim(message)
        return
    elif message.text == '/close':
        adem(message)
        return
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
    elif message.text == '/help':
        adim(message)
        return
    elif message.text == '/close':
        adem(message)
        return
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
bot.infinity_polling()