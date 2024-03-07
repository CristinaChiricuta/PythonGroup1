#Investing Project

#part 1. importing the dataset
import pandas as pd

import requests
apikey = 'K8ZT1SX0ZU8ZOPPH'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey={apikey}'
r = requests.get(url)
data = r.json()
print(data)

print(data.keys())
data = data['Time Series (5min)']
df = pd.DataFrame(data).T.apply(pd.to_numeric)
df.info()
print(df.head())

df.index = pd.DatetimeIndex(df.index)
print(df.head(10))

df.rename(columns = lambda s: s[3:], inplace=True)
print(df.head(10))


# name = input("What is your name? ")
# print("Hi", name, "!")
#
# stock = input("What is the name of the stock you are interested in? ")
# if not stock:
#     print("You did not enter a stock. Please try again.")
# else:
#     r = requests.get(f'https://newsapi.org/v2/top-headlines?country={stock}&apiKey={url}')
#
# if not data ['2. Symbol']:
#     print(f"Cannot find the stock: {stock}")
# else:
#     for symbol in data['2. Symbol']:
#         print(symbol['Time Series (5min)'])
# print(stock)
#
# #price of stock - get last price
#
# my comment