import pandas as pd
import numpy as np

# Ejemplo 1: Usando pandas
df = pd.DataFrame({
    'Edades': [10, 12, 23, 23, 16, 23, 21, 16]
})
print("Ejemplo con pandas:")
print(f"Varianza: {df['Edades'].var()}")  # Muestral (ddof=1 por defecto)
print(f"Desviación estándar: {df['Edades'].std()}")

# Ejemplo 2: Usando NumPy
datos = np.array([10, 12, 23, 23, 16, 23, 21, 16])
print("\nEjemplo con NumPy:")
varianza = np.var(datos)  # Poblacional
desviacion = np.std(datos)  # Poblacional
print(f"Varianza con NumPy: {varianza}")
print(f"Desviación estándar con NumPy: {desviacion}")