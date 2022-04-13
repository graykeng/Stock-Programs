import pandas as pd

# This program simply print the most active 100 stock

url = 'https://finance.yahoo.com/screener/predefined/most_actives?offset=0&count=100'
data = pd.read_html(url)[0]


stk_list = data.Symbol
print(stk_list)
