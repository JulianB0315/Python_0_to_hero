# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs

# Generamos algunos datos ficticios con make_blobs para ilustrar el algoritmo
# Esto crea 100 puntos de datos, distribuidos en 3 clusters (puedes cambiar el número de clusters)
X, _ = make_blobs(n_samples=50, centers=4, cluster_std=0.60, random_state=0)

# Aplicamos el algoritmo de agrupamiento jerárquico aglomerativo
# 'ward' es el método que minimiza la varianza dentro de cada cluster
Z = linkage(X, method='ward')

# Graficamos el dendrograma, que muestra la jerarquía de los clusters
plt.figure(figsize=(12, 10))
dendrogram(Z)
plt.title('Dendrograma del Agrupamiento Jerárquico')
plt.xlabel('Índice de los datos')
plt.ylabel('Distancia')
plt.show()

