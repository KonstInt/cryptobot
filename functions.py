from py_currency_converter import convert
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def cryptoStr(s):
    price = cg.get_price(ids='bitcoin, ethereum, litecoin, tether',
                         vs_currencies=s)
    sym = ''
    if s == 'rub':
        sym = '₽'
    elif s == 'usd':
        sym = '$'
    elif s == 'eur':
        sym = '€'
    elif s == 'cny':
        sym = '¥'
    ss = f'Bitcoin == {price["bitcoin"][s]} {sym}\n\nEthereum == {price["ethereum"][s]} {sym}\n\nLitecoin == {price["litecoin"][s]} {sym}\n\nTether == {price["tether"][s]} {sym}\n\n'
    return ss