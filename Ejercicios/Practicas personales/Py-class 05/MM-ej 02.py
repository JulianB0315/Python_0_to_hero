import numpy as np
import pandas as pd

data_1 = np.array([12, 15, 14, 10, 18, 20, 22, 19, 21])

media = np.mean(data_1)
mediana = np.median(data_1)

print(f'Array original: {data_1}')
print(f'Media: {media:.2f}')
print(f'Mediana: {mediana}')
print('\n' + '-' * 50 + '\n')
df = pd.DataFrame({
    'Nombre': ['Ana', 'Juan', 'Carlos', 'María', 'Luis'],
    'Edad': [23, 25, 30, 27, 22],
    'Salario': [3000, 3200, 2800, 3500, 4000]
})
media_edad = df['Edad'].mean()
mediana_edad = df['Edad'].median()

media_salario = df['Salario'].mean()
mediana_salario = df['Salario'].median()

print(f"Media de edad: {media_edad}")
print(f"Mediana de edad: {mediana_edad}")
print(f"Media de salario: {media_salario}")
print(f"Mediana de salario: {mediana_salario}")