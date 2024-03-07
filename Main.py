
# say hi to user
name = input("What is your name? ")
print("Hi", name, "!")

#import request
import requests
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
r = requests.get(url)
data = r.json()
print(data)

stock = input("What is the name of the stock you are interested in? ")
if not stock:
    print("You did not enter a stock. Please try again.")
else:
    r = requests.get(f'https://newsapi.org/v2/top-headlines?country={stock}&apiKey={url}')

if not data ['2. Symbol']:
    print(f"Cannot find the stock: {stock}")
else:
    for symbol in data['2. Symbol']:
        print(symbol['Time Series (5min)'])
print(stock)

#price of stock - get last price