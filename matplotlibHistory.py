import yfinance as yf
import matplotlib.pyplot as plt

stockA = input("Please enter the first stock symbol: ")
stockB = input("Please enter the second stock symbol: ")

stocks = yf.Tickers(["A", "B"])
hist = stocks.history(period='max')

hist_close = hist['Close']

plt.figure(figsize=(26, 14))
# plt.title('BABA')
hist_close.plot()
plt.show()
# Jun.9
