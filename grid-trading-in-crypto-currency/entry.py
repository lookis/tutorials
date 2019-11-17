import backtrader as bt

import pandas as pd
import numpy as np

class GridStrategy(bt.Strategy):

    def __init__(self):
        self.highest = bt.indicators.Highest(self.data.high, period=1440, subplot=False)
        self.lowest = bt.indicators.Lowest(self.data.low, period=1440, subplot=False)
        mid = (self.highest + self.lowest)/2
        perc_levels = [x for x in np.arange(
            1 + 0.005 * 5, 1 - 0.005 * 5 - 0.005/2, -0.005)]
        self.price_levels = [mid * x for x in perc_levels]
        self.last_price_index = None

    def next(self):
        if self.last_price_index == None:
            for i in range(len(self.price_levels)):
                if self.data.close > self.price_levels[i]:
                    self.last_price_index = i
                    self.order_target_percent(
                        target=i/(len(self.price_levels) - 1))
                    return
        else:
            signal = False
            while True:
                upper = None
                lower = None
                if self.last_price_index > 0:
                    upper = self.price_levels[self.last_price_index - 1]
                if self.last_price_index < len(self.price_levels) - 1:
                    lower = self.price_levels[self.last_price_index + 1]
                # 还不是最轻仓，继续涨，就再卖一档
                if upper != None and self.data.close > upper:
                    self.last_price_index = self.last_price_index - 1
                    signal = True
                    continue
                # 还不是最重仓，继续跌，再买一档
                if lower != None and self.data.close < lower:
                    self.last_price_index = self.last_price_index + 1
                    signal = True
                    continue
                break
            if signal:
                self.long_short = None
                self.order_target_percent(
                    target=self.last_price_index/(len(self.price_levels) - 1))

if __name__ == '__main__':
    # 创建引擎
    cerebro = bt.Cerebro()

    # 加入网格策略
    cerebro.addstrategy(GridStrategy)

    # 导入数据
    df = pd.read_csv('./binance-segment.csv', parse_dates=['time'])
    data = bt.feeds.PandasData(dataname=df,
        timeframe=bt.TimeFrame.Minutes,
        datetime='time',
        open='open',
        high='high',
        low='low',
        close='close',
        volume='volume',
        openinterest=-1)

    cerebro.adddata(data)

    # 设置起始资金
    cerebro.broker.setcash(100000.0)

    # 设定对比指数
    cerebro.addanalyzer(bt.analyzers.TimeReturn, timeframe=bt.TimeFrame.Years,
        data=data, _name='benchmark')

    # 策略收益
    cerebro.addanalyzer(bt.analyzers.TimeReturn, timeframe=bt.TimeFrame.Years, _name='portfolio')

    start_value = cerebro.broker.getvalue()
    print('Starting Portfolio Value: %.2f' % start_value)

    # Run over everything
    results = cerebro.run()

    strat0 = results[0]
    tret_analyzer = strat0.analyzers.getbyname('portfolio')
    print('Portfolio Return:', tret_analyzer.get_analysis())
    tdata_analyzer = strat0.analyzers.getbyname('benchmark')
    print('Benchmark Return:', tdata_analyzer.get_analysis())

    # 画图
    cerebro.plot(style='candle', barup='green')

