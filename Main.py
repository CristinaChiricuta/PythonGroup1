#Investing Project

#Importing packages
import pandas as pd
import requests

#Identifying the user
name = input("What is your username? ")
print("Hi", name, "!")

#Importing the dataset with a function, to get the stock prices
apikey = '12KH3UIJOSJMJ28S'
def get_stock_prices(apikey, symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&outputsize=full&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    # print(data.keys())
    data = data['Time Series (5min)']
    df = pd.DataFrame(data).T.apply(pd.to_numeric)
    # df.info()
    # print(df.head())
    df.index = pd.DatetimeIndex(df.index)
    # print(df.head(10))
    df.rename(columns=lambda s: s[3:], inplace=True)
    return df

#FUNCTIONS

#Creating a function to select the desired stock prices for the user
def select_price(df):
    print("The available prices are: open/high/low/close.")
    selected_price_type = input("Please select your preferred buying price: ").lower()
    selected_price = df[selected_price_type].iloc[0]
    print(f"You have selected the {selected_price_type} price of {symbol} with a value of {selected_price}.")
    return selected_price

#Creating a function to calculate the total price to buy the selected stocks
def buying_price(price, quantity, symbol):
    total_price = price*quantity
    print(f"The total buying price for the stock {symbol} is {total_price}.")

#PROGRAM

#Defining what is the symbol
symbol = input("What is the name of the stock you are interested in? ")

#Calling the get_stock_prices function
stock_prices = get_stock_prices(apikey, symbol)

#Visualizing the latest 10 price changes of the selected stock
print("This is the price evolution of the the stock you have selected in the past hour: \n", stock_prices.head(10))

#Calling the select_price function to display the price of the selected stock
selected_price = select_price(stock_prices)

#Asking the user the quantity of stocks they want to buy, which defines the "quantity" variable for the buying_price function
quantity = int(input("How many stocks do you want to buy at the selected price? "))

#Calling the buying_price function with the variables defined above to get the total price of the selected price, quantity and stock (symbol)
buying_price(selected_price, quantity, symbol)

