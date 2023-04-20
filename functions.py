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

def get_links_news():
    
    # ria
    url_ria = 'https://ria.ru/product_kriptovalyuta/'

    page_ria = requests.get(url_ria).text

    soup_ria = BeautifulSoup(page_ria, 'lxml')

    block_news_ria = soup_ria.find('div', class_ = 'list list-tags')

    first_new_ria = block_news_ria.find_all('div')[0]

    first_new_link_ria = first_new_ria.find('a', href=True)["href"].strip()

    # Habr
    url_habr = 'https://habr.com/ru/search/?q=%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B&target_type=posts&order=date'

    page_habr  = requests.get(url_habr).text

    soup_habr  = BeautifulSoup(page_habr, 'lxml')

    block_news_habr  = soup_habr.find('div', class_ = 'tm-articles-list')

    first_new_habr  = block_news_habr.find_all('article')[0]

    first_new_link_habr  = 'https://habr.com' + first_new_habr.find('a', class_ = 'tm-title__link', href = True)["href"].strip()

    # rcb
    url_rcb = 'https://www.rbc.ru/crypto/tags/?tag=%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B0'

    page_rcb = requests.get(url_rcb).text

    soup_rcb = BeautifulSoup(page_rcb, 'lxml')

    block_news_rcb = soup_rcb.find('div', class_ = 'js-load-container')

    first_new_rcb = block_news_rcb.find_all('div')[0]

    first_new_link_rcb = first_new_rcb.find('a', class_='item__link rm-cm-item-link js-rm-central-column-item-link', href=True)["href"].strip()

    # forklog

    url_forklog = 'https://forklog.com/news'

    page_forklog = requests.get(url_forklog).text

    soup_forklog = BeautifulSoup(page_forklog, 'lxml')

    block_news_forklog = soup_forklog.find('div', class_ = 'category_page_grid')

    first_new_forklog = block_news_forklog.find_all('div')[0]

    first_new_link_forklog = first_new_forklog.find('a', href=True)["href"].strip()

    # bits_media
    url_bits_media = 'https://bits.media/news/'

    page_bits_media = requests.get(url_bits_media).text

    soup_bits_media = BeautifulSoup(page_bits_media, 'lxml')

    block_news_bits_media = soup_bits_media.find('div', id ='main-news')

    first_new_bits_media = block_news_bits_media.find_all('div')[1]

    first_new_link_bits_media = 'https://bits.media/pr/' + first_new_bits_media.find('a', class_ = 'img-box', href=True)["href"].strip()

    # lenta
    url_lenta = 'https://lenta.ru/rubrics/economics/crypto/'

    page_lenta = requests.get(url_lenta).text

    soup_lenta = BeautifulSoup(page_lenta, 'lxml')

    block_news_lenta = soup_lenta.find('ul', class_ ='rubric-page__container _subrubric')

    first_new_lenta = block_news_lenta.find_all('li')[0]

    first_new_link_lenta = 'https://lenta.ru' + first_new_lenta.find('a', class_ = 'card-full-news _subrubric', href=True)["href"].strip()

    links = [first_new_link_ria, first_new_link_habr, first_new_link_rcb, first_new_link_forklog, first_new_link_bits_media, first_new_link_lenta]

    return links