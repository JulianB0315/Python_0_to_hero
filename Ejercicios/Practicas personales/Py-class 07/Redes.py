import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
import yfinance as yf  # Para obtener datos históricos

Sequential = tf.keras.models.Sequential
LSTM = tf.keras.layers.LSTM
Dense = tf.keras.layers.Dense
EarlyStopping = tf.keras.callbacks.EarlyStopping

# 1. Descargar datos de Bitcoin (BTC-USD) desde Yahoo Finance
df = yf.download('BTC-USD', start='2022-01-01', end='2024-01-01')
df = df[['Close']]  # Usamos solo el precio de cierre

# 2. Normalizar datos
scaler = MinMaxScaler(feature_range=(0,1))
df_scaled = scaler.fit_transform(df)

# 3. Preparar datos para LSTM
def crear_secuencias(datos, pasos=60):
    X, y = [], []
    for i in range(len(datos) - pasos):
        X.append(datos[i:i+pasos])
        y.append(datos[i+pasos])
    return np.array(X), np.array(y)

X, y = crear_secuencias(df_scaled)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))  # Reshape para LSTM

# 4. Dividir datos en entrenamiento y prueba (80%-20%)
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# 5. Construir el modelo LSTM
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)),
    LSTM(50, return_sequences=False),
    Dense(25),
    Dense(1)
])

# 6. Compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# 7. Configurar Early Stopping para evitar sobreajuste
early_stopping = EarlyStopping(monitor='loss', patience=5, restore_best_weights=True)

# 8. Entrenar el modelo
print("Entrenando la red neuronal LSTM...")
model.fit(X_train, y_train, epochs=50, batch_size=16, verbose=1, callbacks=[early_stopping])

# 9. Hacer predicciones
predicciones = model.predict(X_test)
predicciones = scaler.inverse_transform(predicciones)  # Desnormalizar

# 10. Evaluación del modelo
y_test_original = scaler.inverse_transform(y_test.reshape(-1,1))
rmse = np.sqrt(mean_squared_error(y_test_original, predicciones))
mape = mean_absolute_percentage_error(y_test_original, predicciones) * 100
precision = 100 - mape

print(f'Error RMSE: {rmse:.2f}')
print(f'Error MAPE: {mape:.2f}%')
print(f'Precisión del modelo: {precision:.2f}%')

# 11. Crear DataFrame de resultados
df_test = df.iloc[-len(y_test):].copy()  # Copia segura para evitar warnings
df_test.loc[:, 'Real'] = y_test_original
df_test.loc[:, 'Predicción'] = predicciones
df_test.loc[:, 'Diferencia'] = df_test['Predicción'] - df_test['Real']
df_test.loc[:, '% Diferencia'] = (df_test['Diferencia'] / df_test['Real']) * 100

# 12. Obtener datos por último día de cada mes
df_meses = df_test.resample('ME').last()[['Real', 'Predicción', 'Diferencia', '% Diferencia']]
print(df_meses)

# 13. Graficar resultados
plt.figure(figsize=(12,6))
plt.plot(df.index[-len(y_test):], y_test_original, label='Real')
plt.plot(df.index[-len(predicciones):], predicciones, label='Predicción', linestyle='dashed')
plt.legend()
plt.title('Predicción del Precio de Bitcoin con LSTM')
plt.xlabel('Fecha')
plt.ylabel('Precio (USD)')
plt.show()
