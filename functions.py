from py_currency_converter import convert
from pycoingecko import CoinGeckoAPI

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