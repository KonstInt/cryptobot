from py_currency_converter import convert
from pycoingecko import CoinGeckoAPI
import requests

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
