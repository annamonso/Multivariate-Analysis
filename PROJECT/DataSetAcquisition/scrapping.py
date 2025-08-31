import yfinance as yf
import pandas as pd
from stocksymbol import StockSymbol
from functools import reduce

symbols_by_country = {}
def tickermap(item):
    symbol = item["symbol"]
    return symbol

def r(a, country):
    try:
        symbol_list = ss.get_symbol_list(market=country)
        symbols_by_country[country] = list(map(tickermap, symbol_list))
        return a
    except:
        return a

api_key = '720a7eb1-c7e4-4db0-ac30-75711eec9686'
ss = StockSymbol(api_key)

countries = ['US','PT','ES','DE', 'AT', 'IT','FR', 'BE','NL','SE','IE','DK','NO','FI','CZ','HU','PL','GR'] 

reduce(r, countries, [])
datos_empresas = []

for country, symbols in symbols_by_country.items():
    i = 0
    print(country)
    for ticker in symbols:
        if i > 500:
            break
        try:
            ticker_yahoo = ticker.lower()
            ticker = ticker.split('.')[0]
            empresa = yf.Ticker(ticker)
            info = empresa.info

            # Get all possible variables and store them in a csv
            data = {}
            for key in info:
                keyname = key
                keyvalue = info[key]
                data[keyname] = keyvalue

            datos_empresas.append(data)
            print(i)
            i += 1

            # Add the new data to the csv
            df = pd.DataFrame(datos_empresas)
            df.to_csv('empresas.csv', index=False)

        except :
            continue

df = pd.DataFrame(datos_empresas)
df.to_csv('empresas.csv', index=False)

