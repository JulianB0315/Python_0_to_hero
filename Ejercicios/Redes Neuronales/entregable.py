# Importación de librerías necesarias
import numpy as np
import tensorflow as tf
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Cargar datos MNIST desde OpenML
mnist = fetch_openml('mnist_784')

# Preprocesamiento: escalado de imágenes a [0, 1]
X = mnist['data'] / 255.0
y = mnist['target'].astype(int)

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# **K-Nearest Neighbors (KNN)**
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predicciones con KNN
y_pred_knn = knn.predict(X_test)

# Evaluación de KNN
print("Evaluación KNN")
print(f"Precisión: {accuracy_score(y_test, y_pred_knn)}")
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred_knn))

# **Red Neuronal Convolucional (CNN)**
# Reestructuración de datos para CNN (debe tener la forma (num_samples, 28, 28, 1))
X_train_cnn = X_train.values.reshape(-1, 28, 28, 1)
X_test_cnn = X_test.values.reshape(-1, 28, 28, 1)

# Creación del modelo CNN
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')  # 10 clases (0-9)
])

# Compilación del modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entrenamiento del modelo CNN
model.fit(X_train_cnn, y_train, epochs=5, validation_data=(X_test_cnn, y_test))

# Evaluación del modelo CNN
test_loss, test_acc = model.evaluate(X_test_cnn, y_test)
print(f"\nPrecisión CNN: {test_acc}")

# **Visualización de resultados**
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.imshow(X_test.iloc[0].values.reshape(28, 28), cmap='gray')
plt.title(f"Predicción KNN: {y_pred_knn[0]}")
plt.subplot(1, 2, 2)
plt.imshow(X_test.iloc[0].values.reshape(28, 28), cmap='gray')
plt.title(f"Predicción CNN: {np.argmax(model.predict(X_test_cnn[0:1]))}")
plt.show()
