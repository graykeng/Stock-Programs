import yfinance as yf
import pandas as pd

# This program simply print the historic dividends and splits with date
pd.set_option('display.max_rows', 500)
stock = input('Enter a stock ticker symbol: ')
data = yf.Ticker(stock)
a = data.actions
print(a)
