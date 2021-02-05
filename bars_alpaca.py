import pandas as pd
import alpaca_trade_api as tradeapi
from datetime import datetime, timedelta
import config

api = tradeapi.REST(config.KEY, config.SECRET_KEY, "https://data.alpaca.markets/v1")

symbols = []
qqq = open('qqq.csv', 'r')
for line in qqq.readlines()[1:]:
    symbols.append(line.split(',')[2].strip())
frames = []
symbols = ['AAPL']
for symbol in symbols:
    week = timedelta(days=7)
    start_date = datetime(2021, 1, 1)
    last_date = datetime(2021, 2, 10)
    end_date = start_date + timedelta(days=4)
    historic_data = api.polygon.historic_agg_v2(symbol, 1, 'day', _from=start_date, to=end_date).df

    while start_date < last_date:
        start_date = start_date + week
        end_date = end_date + week
        historic_data = pd.concat([historic_data,api.polygon.historic_agg_v2(symbol, 1, 'day', _from= start_date, to= end_date).df])

    frames.append(historic_data)
    print(symbol)

    
    

