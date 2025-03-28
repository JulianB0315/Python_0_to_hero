import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import tensorflow as tf
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.arima.model import ARIMA
Sequential = tf.keras.models.Sequential
LSTM = tf.keras.layers.LSTM
Dense = tf.keras.layers.Dense
EarlyStopping = tf.keras.callbacks.EarlyStopping

# Descargar datos históricos de Bitcoin
data = yf.download('BTC-USD', start='2022-01-01', end='2024-01-01')
data = data[['Close']]  # Solo nos interesa el precio de cierre

# Convertir el índice en columna de fecha
data.reset_index(inplace=True)
data['Date'] = pd.to_datetime(data['Date'])

# Convertir fechas a valores numéricos para regresión lineal
data['Days'] = (data['Date'] - data['Date'].min()).dt.days

# Dividir en entrenamiento (80%) y prueba (20%)
train_size = int(len(data) * 0.8)
train, test = data.iloc[:train_size], data.iloc[train_size:]

# 📌 Modelo 1: ARIMA
arima_model = ARIMA(train['Close'], order=(5,1,0)).fit()
arima_pred = arima_model.forecast(steps=len(test))

# 📌 Modelo 2: Regresión Lineal
lr = LinearRegression()
lr.fit(train[['Days']], train['Close'])
lr_pred = lr.predict(test[['Days']])

# 📌 Modelo 3: LSTM
scaler = MinMaxScaler(feature_range=(0, 1))
train_scaled = scaler.fit_transform(train[['Close']])

X_train, y_train = [], []
for i in range(10, len(train_scaled)):
    X_train.append(train_scaled[i-10:i, 0])
    y_train.append(train_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Definir modelo LSTM
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    LSTM(50),
    Dense(1)
])
model.compile(optimizer='adam', loss='mean_squared_error')

# Entrenar modelo
model.fit(X_train, y_train, epochs=10, batch_size=16, verbose=0)

# Preparar datos de prueba para LSTM
test_scaled = scaler.transform(test[['Close']])
X_test, y_test = [], test_scaled[10:]
for i in range(10, len(test_scaled)):
    X_test.append(test_scaled[i-10:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Predicción con LSTM
lstm_pred = model.predict(X_test)
lstm_pred = scaler.inverse_transform(lstm_pred)

# 📊 Gráfico Comparativo
plt.figure(figsize=(12, 6))
plt.plot(test['Date'], test['Close'], label='Real', color='black')
plt.plot(test['Date'], arima_pred, label='ARIMA', linestyle='dashed', color='red')
plt.plot(test['Date'], lr_pred, label='Regresión Lineal', linestyle='dashed', color='blue')
plt.plot(test['Date'][10:], lstm_pred, label='LSTM', linestyle='dashed', color='green')
plt.xlabel('Fecha')
plt.ylabel('Precio BTC (USD)')
plt.title('Comparación de Modelos de Predicción')
plt.legend()
plt.show()
