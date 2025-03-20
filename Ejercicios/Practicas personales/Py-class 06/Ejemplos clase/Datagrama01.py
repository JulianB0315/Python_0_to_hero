
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=10, centers=2, cluster_std=0.60, random_state=0)
# Ejemplo de datos (10 puntos en 2 dimensiones)
mis_datos = np.array([
    [1.2, 1.6],
    [1.3, 2.1],
    [3.4, 4.5],
    [3.5, 4.6],
    [7.2, 8.3],
    [7.4, 8.5],
    [8.1, 7.2],
    [8.2, 7.5],
    [9.1, 9.2],
    [9.3, 19.4]
])

# Ahora, puedes aplicar el algoritmo de agrupamiento jerárquico a estos datos
Z = linkage(mis_datos, method='ward')

# Y graficar el dendrograma
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title('Dendrograma del Agrupamiento Jerárquico')
plt.xlabel('Índice de los datos')
plt.ylabel('Distancia')
plt.show()
