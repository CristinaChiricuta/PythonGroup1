#Investing Project

#Importing packages
import pandas as pd
import requests

#Identifying the user
name = input("What is your username? ")
print("Hi", name, "!")

#Importing the dataset
#Asking the user which stock they want
apikey = '12KH3UIJOSJMJ28S'
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

#2. Asking the user which token they want to select

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

#price of stock - get last price

#FUNCTION THAT RUNS EVERYTHING AGAIN (DO YOU WANT TO BUY MORE?)
def buy_stocks():
    while True:
        user_input = input("Do you want to buy more stocks? (yes/no): ")

        if user_input == 'yes':
            symbol = input("Enter the stock symbol: ")
            print(f"You have chosen to buy stocks with symbol: {symbol}")
            # Add logic for 1. RETRIEVE BUY PRICE + INPUT QUANTITY + WRITE A FUNCTION BUYING PRICE*QUANTITY
            #function price at point 1()

        elif user_input == 'no':
            print("Goodbye! Have a great day.")
            break

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

buy_stocks()
