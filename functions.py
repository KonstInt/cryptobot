from py_currency_converter import convert
from pycoingecko import CoinGeckoAPI
import requests
from bs4 import BeautifulSoup

cg = CoinGeckoAPI()


def cryptoStr(s):
    price = cg.get_price(ids='bitcoin, ethereum, litecoin, tether',
                         vs_currencies=s)
    sym = symF(s)
    ss = f'Bitcoin == {price["bitcoin"][s]} {sym}\n\nEthereum == {price["ethereum"][s]} {sym}\n\nLitecoin == {price["litecoin"][s]} {sym}\n\nTether == {price["tether"][s]} {sym}\n\n'
    return ss

def valuteStr(k1, s):
    price = convert(base = k1, amount = 1, to=[s])
    sym1 = symF(k1)
    sym2 = symF(s)
    ss = f'1{sym1} = {price[s]}{sym2}'
    return ss

def symF(s):
    s = s.lower()
    sym = ''
    if s == 'rub':
        sym = '₽'
    elif s == 'usd':
        sym = '$'
    elif s == 'eur':
        sym = '€'
    elif s == 'cny':
        sym = '¥'
    return sym


def depth_find(coin1="btc", coin2="usd"):
    response = requests.get(url=f"https://yobit.net/api/3/depth/{coin1}_{coin2}?limit=150&ignore_invalid=1")

    with open("depth.txt", "w") as file:
        file.write(response.text)

    bids = response.json()[f"{coin1}_usd"]["bids"]

    total_bids_amount = 0
    for item in bids:
        price = item[0]
        coin_amount = item[1]

        total_bids_amount += price * coin_amount

    return f"Сумма выставленных на продажу {coin1}: {round(total_bids_amount, 3)} $"

def trades_find_ask(coin1="btc", coin2="usd"):
    response = requests.get(url=f"https://yobit.net/api/3/trades/{coin1}_{coin2}?limit=150&ignore_invalid=1")

    with open("trades.txt", "w") as file:
        file.write(response.text)

    total_trade_ask = 0

    for item in response.json()[f"{coin1}_{coin2}"]:
        if item["type"] == "ask":
            total_trade_ask += item["price"] * item["amount"]

    info = f"Общая сумма проданных {coin1} : {round(total_trade_ask, 3)} $"

    return info

def trades_find_bid(coin1="btc", coin2="usd"):
    response = requests.get(url=f"https://yobit.net/api/3/trades/{coin1}_{coin2}?limit=150&ignore_invalid=1")

    with open("trades.txt", "w") as file:
        file.write(response.text)

    total_trade_bid = 0

    for item in response.json()[f"{coin1}_{coin2}"]:
        if item["type"] == "bid":
            total_trade_bid += item["price"] * item["amount"]


    info = f"Общая сумма купленных {coin1} : {round(total_trade_bid, 3)} $"

    return info

# ria

def get_link_first_new_ria():
    url = 'https://ria.ru/product_kriptovalyuta/'

    page = requests.get(url).text

    soup = BeautifulSoup(page, 'lxml')

    block_news = soup.find('div', class_ = 'list list-tags')

    first_new = block_news.find_all('div')[0]

    first_new_link = first_new.find('a', href=True)["href"].strip()

    return first_new_link



# Хабр

def get_link_first_new_habr():
    url = 'https://habr.com/ru/search/?q=%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B&target_type=posts&order=date'

    page = requests.get(url).text

    soup = BeautifulSoup(page, 'lxml')

    block_news = soup.find('div', class_ = 'tm-articles-list')

    first_new = block_news.find_all('article')[0]

    first_new_link = 'https://habr.com' + first_new.find('a', class_ = 'tm-title__link', href = True)["href"].strip()

    return first_new_link




# rcb

def get_link_first_new_rcb():
    url = 'https://www.rbc.ru/crypto/tags/?tag=%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B0'

    page = requests.get(url).text

    soup = BeautifulSoup(page, 'lxml')

    block_news = soup.find('div', class_ = 'js-load-container')

    first_new = block_news.find_all('div')[0]

    first_new_link = first_new.find('a', class_='item__link rm-cm-item-link js-rm-central-column-item-link', href=True)["href"].strip()

    return first_new_link



# forklog

def get_link_first_new_forklog():
    url = 'https://forklog.com/news'

    page = requests.get(url).text

    soup = BeautifulSoup(page, 'lxml')

    block_news = soup.find('div', class_ = 'category_page_grid')

    first_new = block_news.find_all('div')[0]

    first_new_link = first_new.find('a', href=True)["href"].strip()

    return first_new_link

# bits.media

def get_link_first_new_bits():
    url = 'https://bits.media/news/'

    page = requests.get(url).text

    soup = BeautifulSoup(page, 'lxml')

    block_news = soup.find('div', id ='main-news')

    first_new = block_news.find_all('div')[1]

    first_new_link = 'https://bits.media/pr/' + first_new.find('a', class_ = 'img-box', href=True)["href"].strip()

    return first_new_link

# lenta

def get_link_first_new_lenta():
    url = 'https://lenta.ru/rubrics/economics/crypto/'

    page = requests.get(url).text

    soup = BeautifulSoup(page, 'lxml')

    block_news = soup.find('ul', class_ ='rubric-page__container _subrubric')

    first_new = block_news.find_all('li')[0]

    first_new_link = 'https://lenta.ru' + first_new.find('a', class_ = 'card-full-news _subrubric', href=True)["href"].strip()

    return first_new_link