import ccxt
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# تابع برای دریافت داده‌های بازار
def fetch_market_data(symbol, timeframe, limit):
    exchange = ccxt.binance()
    data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# تابع برای آماده‌سازی داده‌ها برای شبکه عصبی
def prepare_data_for_nn(df, look_back):
    dataset = df['close'].values.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset = scaler.fit_transform(dataset)
    X, y = [], []
    for i in range(look_back, len(dataset)):
        X.append(dataset[i-look_back:i, 0])
        y.append(dataset[i, 0])
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    return X, y, scaler

# تابع برای ساخت و آموزش مدل شبکه عصبی
def build_and_train_nn(X_train, y_train):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    early_stopping = EarlyStopping(monitor='loss', patience=5, verbose=1, mode='auto')
    model.fit(X_train, y_train, epochs=100, batch_size=32, callbacks=[early_stopping])
    return model

# مثال استفاده از توابع
if name == "main":
    symbol = 'BTC/USDT'
    timeframe = '1d'
    limit = 100
    look_back = 10

    # دریافت داده‌های بازار
    market_data = fetch_market_data(symbol, timeframe, limit)

    # آماده‌سازی داده‌ها برای شبکه عصبی
    X, y, scaler = prepare_data_for_nn(market_data, look_back)

    # ساخت و آموزش مدل شبکه عصبی
    model = build_and_train_nn(X, y)

    # استفاده از مدل برای پیش‌بینی قیمت
    last_data = market_data['close'].tail(look_back).values.reshape(-1, 1)
    scaled_last_data = scaler.transform(last_data)
    X_test = np.array([scaled_last_data])
    predicted_price = model.predict(X_test)
    predicted_price = scaler.inverse_transform(predicted_price)
    print("Predicted price:", predicted_price)