from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

stock = input("Enter the stock symbol: ")

data = pdr.get_data_yahoo(stock, start='2000-01-01')
print(data)
# Jun.9
