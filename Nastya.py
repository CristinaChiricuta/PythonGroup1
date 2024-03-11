#Investing Project

#Importing packages
import pandas as pd
import requests

#Identifying the user
name = input("What is your username? ")
print("Hi", name, "!")

#Importing the dataset
#Asking the user which stock they want
apikey = 'K8ZT1SX0ZU8ZOPPH'
symbol = input("What is the name of the stock you are interested in? ")
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&outputsize=full&apikey={apikey}'
r = requests.get(url)
data = r.json()
# print(data)

# print(data.keys())
data = data['Time Series (5min)']
df = pd.DataFrame(data).T.apply(pd.to_numeric)
# df.info()
# print(df.head())

#Visualizing the latest 10 price changes of the selected stock
df.index = pd.DatetimeIndex(df.index)
# print(df.head(10))
df.rename(columns = lambda s: s[3:], inplace=True)
print(df.head(10))

# create a wallet
wallet = 10000

# retrieve the last available price
current_price = df.iloc[-1]['close']

# retrieve the buying price
buying_price = current_price  # TO BE REPLACED BY INPUT FUNCTION FROM LETIZIA

# define how much to buy
amount = 1  # TO BE REPLACED BY INPUT FUNCTION FROM LETIZIA

# calculate the balance per stock now
cost_for_stock = buying_price * amount

# create a dictionary to store information about stocks in the user's portfolio
portfolio = {}
portfolio[symbol] = [buying_price, current_price, amount, cost_for_stock]

# add each stock bought to the stocks_in_portfolio
wallet = wallet - balance_per_stock_now

# add each stock bought to the stocks_in_portfolio
print(wallet, stocks_in_portfolio)