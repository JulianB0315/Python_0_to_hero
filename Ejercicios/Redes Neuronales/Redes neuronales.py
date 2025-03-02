import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Cargar el dataset MNIST (imágenes de dígitos escritos a mano)
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar los valores de los píxeles de 0-255 a 0-1 para mejorar el entrenamiento
x_train, x_test = x_train / 255.0, x_test / 255.0

# Definir la arquitectura de la red neuronal
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Convierte la imagen 28x28 en un vector de 784 valores
    keras.layers.Dense(128, activation='relu'),  # Capa oculta con 128 neuronas y activación ReLU
    keras.layers.Dropout(0.2),  # Dropout del 20% para evitar sobreajuste
    keras.layers.Dense(10, activation='softmax')  # Capa de salida con 10 neuronas para las 10 clases (0-9)
])

# Compilar el modelo (configurar el optimizador, la función de pérdida y la métrica de evaluación)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entrenar la red neuronal con los datos de entrenamiento
model.fit(x_train, y_train, epochs=5)

# Evaluar el modelo en los datos de prueba
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Precisión en test: {test_acc:.4f}')

# Hacer predicciones con el modelo entrenado
predictions = model.predict(x_test)

# Mostrar una imagen con la predicción del modelo
plt.imshow(x_test[0], cmap='gray')  # Muestra la primera imagen del conjunto de prueba
plt.title(f'Predicción: {np.argmax(predictions[0])}')  # Muestra la predicción realizada por la red
plt.savefig(f'Predicción_{np.argmax(predictions[0])}.png')  # Guardar la figura en un archivo
plt.close()  # Cerrar la figura