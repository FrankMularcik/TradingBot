#This program imports a file with strategy classes and a file with price data
#Then it runs cerebro and backtrader which backtests a portfolio based on the strategy and data given
import backtrader as bt
import datetime 
import strategies
import pandas as pd
import bars_alpaca


starting_values = 0
ending_values = 0
output = open('backtrade.txt', 'w+')
for i in range(len(bars_alpaca.frames)):
    cerebro = bt.Cerebro()
    data = bt.feeds.PandasData(dataname=bars_alpaca.frames[i])

    cerebro.adddata(data)

    cerebro.addstrategy(strategies.MyStrat)
    
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
