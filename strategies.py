import backtrader as bt

class MyStrat(bt.Strategy):

    def notify_fund(self, cash, value, fundvalue, shares):
        self.cash = cash 

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        
        if order.status in [order.Completed]:
            # if order.isbuy():
            #     self.log("BOUGHT %i SHARES at $%.2f" % (order.executed.size, order.executed.price))
                

            # elif order.issell():
            #     self.log("SOLD %i SHARES at $%.2f" % (order.executed.size, order.executed.price))
                
            self.shares = self.shares + order.executed.size
        self.order = None

    def __init__(self):
        self.order = None
        self.shares = 0
        self.cash = 0
        
    def next(self):
        if self.order:
            return
        
        #if self.cash > 0:

        #if buy condition
        #     if self.cross[0] > 0:
        #         #self.log("BUY CREATED at $%.2f" % self.data.close[0])
        #         self.order = self.buy(size=int(self.cash*0.50/self.data.close[0]))

        #if sell condition                                                
        #if self.shares > 0:
        #     if self.cross[0] < 0: 
        #         #self.log("SELL CREATED at $%.2f" % self.data.close[0])
        #         self.order = self.sell(size=int(self.shares*0.50))
            
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print("%s, %s" % (dt.isoformat(), txt))


class MacdStrat(MyStrat):
    
    def __init__(self):
        self.macd = bt.indicators.MACD(self.data.close)
        self.cross = bt.indicators.CrossOver(self.macd.macd, self.macd.signal)
        self.order = None
        self.shares = 0
        self.cash = 0
        print(self.cross)
   
    def next(self):
        if self.order:
            return

        if self.cash > 0:
            if self.cross[0] > 0:
                #self.log("BUY CREATED at $%.2f" % self.data.close[0])
                self.order = self.buy(size=int(self.cash*0.50/self.data.close[0]))
                                                   
        if self.shares > 0:
            if self.cross[0] < 0: 
                #self.log("SELL CREATED at $%.2f" % self.data.close[0])
                self.order = self.sell(size=int(self.shares*0.50))


class SmaStrat(MyStrat):

    def _init__(self):
        self.sma_20 = bt.indicators.MovingAverageSimple(self.data.close, period=20)
        self.sma_50 = bt.indicators.MovingAverageSimple(self.data.close, period=50)
        #self.cross = bt.indicators.CrossOver(sma_20, sma_50)
        #super().__init__()

    def next(self):
        print(self.sma_20[0])
        if self.order:
            return

        # if self.cash > 0:
        #     if self.cross[0] > 0:
        #         #self.log("BUY CREATED at $%.2f" % self.data.close[0])
        #         self.order = self.buy(size=int(self.cash*0.50/self.data.close[0]))
                                                   
        # if self.shares > 0:
        #     if self.cross[0] < 0: 
        #         #self.log("SELL CREATED at $%.2f" % self.data.close[0])
        #         self.order = self.sell(size=int(self.shares*0.50))


#d = MyStrat()