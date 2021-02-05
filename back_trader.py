import backtrader as bt
import datetime 
import strategies
import pandas as pd
import bars_alpaca

#data_path = 'AAPL_1min_sample.csv'
#data_file = pd.read_csv(data_path, index_col='Date', parse_dates=True)

    


# data = backtrader.feeds.YahooFinanceCSVData(
#     dataname=data_path,
#     # Do not pass values before this date
#     fromdate=datetime.datetime(2016, 1, 1),
#     # Do not pass values after this date
#     todate=datetime.datetime(2021, 12, 31),
#     reverse=False)
starting_values = 0
ending_values = 0
output = open('backtrade.txt', 'w+')
for i in range(len(bars_alpaca.frames)):
    cerebro = bt.Cerebro()
    data = bt.feeds.PandasData(dataname=bars_alpaca.frames[i])

    cerebro.adddata(data)

    cerebro.addstrategy(strategies.MyStrat)
    #cerebro.broker.set_fundstartval(0)
    cerebro.broker.set_cash(100000)
    #print("Current Portfolio Value: %.2f" % cerebro.broker.getvalue())
    ticker_start = cerebro.broker.getvalue()
    starting_values = starting_values + ticker_start
    result = cerebro.run()

    #print("Current Portfolio Value: %.2f" % cerebro.broker.getvalue())
    ticker_end = cerebro.broker.getvalue()
    ending_values = ending_values + ticker_end
    #cerebro.plot()
    output.write('{} return of {:.2f}%\n'.format(bars_alpaca.symbols[i], (ticker_end*100/ticker_start)-100))
    print(i)
    
output.write('Total return of {:.2f}%'.format((ending_values*100/starting_values)-100))
