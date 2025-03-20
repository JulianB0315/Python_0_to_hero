# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generamos un conjunto de datos ficticio (100 puntos en 3 clusters)
X, _ = make_blobs(n_samples=100, centers=3, cluster_std=0.60, random_state=0)

# Creamos el modelo K-Means con 3 clusters (puedes cambiar el número de clusters)
kmeans = KMeans(n_clusters=3)

# Ajustamos el modelo a los datos
kmeans.fit(X)

# Obtenemos las etiquetas (el cluster al que pertenece cada punto)
etiquetas = kmeans.labels_

# Obtenemos los centroides de los clusters
centroides = kmeans.cluster_centers_

# Visualizamos los resultados
plt.scatter(X[:, 0], X[:, 1], c=etiquetas, cmap='viridis')
plt.scatter(centroides[:, 0], centroides[:, 1], s=200, c='red', marker='X')  # Centroides en rojo
plt.title('Resultado de K-Means')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()
