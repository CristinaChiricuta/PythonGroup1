#Importing packages
import pandas as pd
import requests

#Initializing global variable
wallet = 0
portfolio = {}

#Identifying the user
name = input("What is your username? ")
print("Hi", name, "!")
wallet = int(input('Please enter your initial deposit in $: '))

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
def select_price(df,  symbol):
    global wallet
    print("The available prices are: open/high/low/close.")
    selected_price_type = input("Please select your preferred buying price: ").lower()
    if selected_price_type in df.columns:
        selected_price = df[selected_price_type].iloc[0]
        print(f"You have selected the {selected_price_type} price of {symbol} with a value of {selected_price}$.")
        print(
            f"You have {round(wallet, 2)}$ amount on your wallet. Please, be aware, you can't buy stocks for a bigger amount, than you have in your wallet")
        return selected_price
    else:
        print("Invalid price type selected.")
        return None

#Creating a function to calculate the total price to buy the selected stocks
def buying_price(price, quantity, symbol):
    global wallet
    total_price = price * quantity
    portfolio[symbol] = [price, quantity, total_price]
    if total_price<=wallet:
        print(f"The total buying price for the stock {symbol} is {round(total_price, 2)}$.")
        wallet = wallet - total_price
        total_balance_portfolio = sum(portfolio[s][2] for s in portfolio)
        print("You have the following stocks in your portfolio:", list(portfolio.keys()))
        for stock in portfolio:
            print (f"You have bought {round(portfolio[stock][1],2)} stocks of {stock} for the price of {round(portfolio[stock][0],2)}$")
        print(f'Cash left in your wallet: {round(wallet,2)}$. The total balance of your portfolio is: {round(total_balance_portfolio,2)}$')
        return total_price
    else:
        print("You don't have enough money to buy stocks")

#3. FUNCTION THAT RUNS EVERYTHING AGAIN (DO YOU WANT TO BUY MORE?)
def buy_sell_stocks():
    global wallet
    while True:
        user_input = input("Do you want to buy stocks, sell stocks, or add cash to the wallet? (buy/sell/add cash/exit): ")

        if user_input == 'buy':
            new_purchase = input("Enter the stock symbol: ")
            new_stock_prices = get_stock_prices(apikey,new_purchase)
            if new_stock_prices is not None:
                print(f"You have chosen to buy stocks with symbol: {new_purchase}")
                print("This is the price evolution of the the stock you have selected in the past hour: \n",
                      new_stock_prices.head(10))
                new_price = select_price(new_stock_prices, new_purchase)
                quantity = int(input("How many stocks do you want to buy at the selected price? "))
                total = buying_price(new_price, quantity, new_purchase)
        elif user_input == 'sell':
            symbol_to_sell = input("Enter the stock symbol you want to sell: ")
            print (f"Now you have {portfolio[symbol_to_sell][1]} stocks of {symbol_to_sell} in your portfolio")
            quantity_to_sell = int(input("Enter the quantity of stocks to sell: "))
            stock_prices_to_sell = get_stock_prices(apikey, symbol_to_sell)
            if stock_prices_to_sell is not None:
                sell_stock(symbol_to_sell, quantity_to_sell, stock_prices_to_sell)
            else:
                continue
        elif user_input == 'add cash':
            print (f"The current amount in your wallet is {round(wallet,2)}$")
            add_cash = int(input("Please enter the amount of money that you want to add to the wallet: "))
            wallet += add_cash
            print (f"Your updated balance in the wallet is {round(wallet)}$")
        elif user_input == 'exit':
            print("Goodbye! Have a great day.")
            break

        else:
            print("Invalid input. Please enter 'buy', 'sell', 'add cash' or 'exit'")


# Creating a function to sell stocks from the wallet
def sell_stock(symbol, quantity, stock_prices):
    global wallet
    if symbol not in portfolio or portfolio[symbol][1] < quantity:
        print(f"Error: Insufficient stocks of {symbol} in the portfolio.")
        return None

    # Get the current stock price from the DataFrame
    current_price = stock_prices['close'].iloc[0]

    # Calculate the total selling price
    total_selling_price = current_price * quantity

    # Update the wallet by adding the total selling price
    wallet += total_selling_price
    total_balance_portfolio = sum(portfolio[s][2] for s in portfolio)
    total_balance_portfolio -= total_selling_price

    # Update the portfolio by subtracting the sold quantity
    portfolio[symbol][1] -= quantity

    print(f"Sold {quantity} stocks of {symbol} at ${current_price} each. Total selling price: ${total_selling_price}")
    for stock in portfolio:
        print(
            f"You have {round(portfolio[stock][1], 2)} stocks of {stock} in your portfolio")
    print(
        f'You have the following amount left on your wallet: {round(wallet, 2)}$. The total balance of your portfolio is {round(total_balance_portfolio, 2)}$')
    return total_selling_price

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
buy_sell_stocks()
