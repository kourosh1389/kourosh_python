# Import libraries
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Load and preprocess the data
df = pd.read_csv("arz_price.csv") # The CSV file contains the date and price of arz in IRR from 2016 to 2021
df = df.dropna() # Drop any missing values
df = df.set_index("Date") # Set the date as the index
df = df.sort_index() # Sort the data by date
df = df[["Price"]] # Select only the price column
df.head() # Show the first five rows138913

# Plot the data
plt.figure(figsize=(15, 10))
plt.title("Arz Price in IRR")
plt.xlabel("Date")
plt.ylabel("Price")
plt.plot(df)
plt.show()

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1)) # Create a scaler object
df_scaled = scaler.fit_transform(df) # Fit and transform the data to the range (0, 1)

# Split the data into train and test sets
train_size = int(len(df_scaled) * 0.8) # Use 80% of the data for training
test_size = len(df_scaled) - train_size # Use the remaining 20% for testing
train, test = df_scaled[0:train_size, :], df_scaled[train_size:len(df_scaled), :] # Split the data

# Create a function to convert the data into sequences of a given length
def create_sequences(data, seq_length):
  x = [] # The input sequences
  y = [] # The output sequences
  for i in range(len(data) - seq_length - 1):
    # Take a sequence of length seq_length as input
    x_seq = data[i:(i + seq_length), 0]
    # Take the next value as output
    y_seq = data[i + seq_length, 0]
    # Append to the lists
    x.append(x_seq)
    y.append(y_seq)
  # Convert to numpy arrays
  x = np.array(x)
  y = np.array(y)
  return x, y

# Define the sequence length
seq_length = 10 # Use 10 previous values to predict the next one

# Create the train and test sequences
x_train, y_train = create_sequences(train, seq_length)
x_test, y_test = create_sequences(test, seq_length)

# Reshape the input sequences to the format (batch_size, time_steps, features)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# Build the RNN model
model = Sequential() # Create a sequential model
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1))) # Add a LSTM layer with 50 units and return the sequences
model.add(Dropout(0.2)) # Add a dropout layer to prevent overfitting
model.add(LSTM(50, return_sequences=False)) # Add another LSTM layer with 50 units and do not return the sequences
model.add(Dropout(0.2)) # Add another dropout layer
model.add(Dense(1)) # Add a dense layer with one unit as the output
model.compile(loss="mean_squared_error", optimizer="adam") # Compile the model with mean squared error as the loss function and adam as the optimizer

# Train the model
model.fit(x_train, y_train, epochs=100, batch_size=32, verbose=1) # Fit the model on the train data for 100 epochs and a batch size of 32

# Evaluate the model
model.evaluate(x_test, y_test) # Evaluate the model on the test data

# Make predictions
y_pred = model.predict(x_test) # Predict the values for the test data
y_pred = scaler.inverse_transform(y_pred) # Inverse transform the predictions to the original scale
y_test = scaler.inverse_transform([y_test]) # Inverse transform the test data to the original scale

# Plot the actual vs predicted values
plt.figure(figsize=(15, 10))
plt.title("Arz Price Prediction")
plt.xlabel("Date")
plt.ylabel("Price")
plt.plot(y_test[0], label="Actual")
plt.plot(y_pred, label="Predicted")
plt.legend()
plt.show()