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
    if 'Time Series (5min)' in data:
        data = data['Time Series (5min)']
        df = pd.DataFrame(data).T.apply(pd.to_numeric)
        df.index = pd.to_datetime(df.index)
        df.rename(columns=lambda s: s[3:], inplace=True)
        return df
    else:
        print("Error: Unable to fetch data. Please check the symbol or try again later.")
        return None

#FUNCTIONS

#Creating a function to select the desired stock prices for the user
def select_price(df, symbol):
    print("The available prices are: open/high/low/close.")
    selected_price_type = input("Please select your preferred buying price: ").lower()
    if selected_price_type in df.columns:
        selected_price = df[selected_price_type].iloc[0]
        print(f"You have selected the {selected_price_type} price of {symbol} with a value of {selected_price}.")
        return selected_price
    else:
        print("Invalid price type selected.")
        return None

#Creating a function to calculate the total price to buy the selected stocks
def buying_price(price, quantity, symbol):
    total_price = price * quantity
    print(f"The total buying price for the stock {symbol} is {total_price}.")
    return total_price

#3. FUNCTION THAT RUNS EVERYTHING AGAIN (DO YOU WANT TO BUY MORE?)
def buy_stocks():
    while True:
        user_input = input("Do you want to buy more stocks? (yes/no): ")

        if user_input == 'yes':
            new_purchase = input("Enter the stock symbol: ")
            new_stock_prices = get_stock_prices(apikey,new_purchase)
            if new_stock_prices is not None:
                print(f"You have chosen to buy stocks with symbol: {new_purchase}")
                print("This is the price evolution of the the stock you have selected in the past hour: \n",
                      new_stock_prices.head(10))
                new_price = select_price(new_stock_prices, new_purchase)
                quantity = int(input("How many stocks do you want to buy at the selected price? "))
                total = buying_price(new_price, quantity, new_purchase)
            else:
                continue

        elif user_input == 'no':
            print("Goodbye! Have a great day.")
            break

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
#PROGRAM

#first purchase

#Defining what is the symbol
symbol = input("What is the name of the stock you are interested in? ")

#Calling the get_stock_prices function
stock_prices = get_stock_prices(apikey, symbol)

#Visualizing the latest 10 price changes of the selected stock
if stock_prices is not None:
    print("This is the price evolution of the the stock you have selected in the past hour: \n", stock_prices.head(10))

    #Calling the select_price function to display the price of the selected stock
    selected_price = select_price(stock_prices, symbol)

    #Asking the user the quantity of stocks they want to buy, which defines the "quantity" variable for the buying_price function
    quantity = int(input("How many stocks do you want to buy at the selected price? "))

    #Calling the buying_price function with the variables defined above to get the total price of the selected price, quantity and stock (symbol)
    buying_price(selected_price, quantity, symbol)

#new purchase

#calling if you want to buy more
buy_stocks()