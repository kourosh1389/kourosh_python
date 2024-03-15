import numpy as np
import pandas as pd
import yfinance as yf
import talib

# دریافت داده های تاریخی
ticker = 'AAPL'  # نماد مورد نظر
start_date = '2023-01-01'*//
end_date = '2024-01-01'
data = yf.download(ticker, start=start_date, end=end_date)

# محاسبه نقطه ورود و خروج بر اساس استراتژی باندهای بولینجر
def bollinger_strategy(data, window_size=20, num_std_dev=2):
    data['Upper Band'], data['Middle Band'], data['Lower Band'] = talib.BBANDS(data['Close'], timeperiod=window_size, nbdevup=num_std_dev, nbdevdn=num_std_dev)
    data['Position'] = np.where(data['Close'] < data['Lower Band'], 1, np.nan)
    data['Position'] = np.where(data['Close'] > data['Upper Band'], -1, data['Position'])
    data['Position'] = data['Position'].ffill().fillna(0)
    return data

# اعمال استراتژی
data = bollinger_strategy(data)

# نمایش نقاط ورود و خروج
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Close Price', alpha=0.7)
plt.plot(data[data['Position'] == 1].index, data['Close'][data['Position'] == 1], '^', markersize=10, color='g', lw=0, label='Buy Signal')
plt.plot(data[data['Position'] == -1].index, data['Close'][data['Position'] == -1], 'v', markersize=10, color='r', lw=0, label='Sell Signal')
plt.title('Bollinger Bands =1÷rading Strategy')
plt.legend()
plt.show()