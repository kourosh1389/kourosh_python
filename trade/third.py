import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# بارگیری و پردازش داده‌های بازار فارکس
data = pd.read_csv('forex_data.csv')

# پیش‌پردازش داده‌ها

# تقسیم داده‌ها به ویژگی‌ها و برچسب‌ها
X = data.drop(columns=['target_column'])  # تعیین ویژگی‌ها
y = data['target_column']  # تعیین برچسب‌ها

# تقسیم داده‌ها به مجموعه‌های آموزش و آزمون
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# استانداردسازی داده‌ها
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# تبدیل داده به فرمت سریهای زمانی
def create_time_series(data, time_steps):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:(i + time_steps)])
        y.append(data[i + time_steps])
    return np.array(X), np.array(y)

time_steps = 10  # تعیین مقدار تایم‌ستپ
X_train_series, y_train_series = create_time_series(X_train_scaled, time_steps)
X_test_series, y_test_series = create_time_series(X_test_scaled, time_steps)

# پیاده‌سازی مدل با استفاده از یک شبکه LSTM
model = Sequential([
    LSTM(units=64, input_shape=(X_train_series.shape[1], X_train_series.shape[2]), return_sequences=True),
    Dropout(0.2),
    LSTM(units=64),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(1)
])

model.compile(optimizer=Adam(), loss='mean_squared_error')

# آموزش مدل
model.fit(X_train_series, y_train_series, epochs=100, batch_size=32, validation_split=0.1)

# ارزیابی مدل
y_pred = model.predict(X_test_series)
mse = mean_squared_error(y_test_series, y_pred)
print("Mean Squared Error:", mse)