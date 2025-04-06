import statistics

# Lista de números
datos = [10, 12, 23, 23, 16, 23, 21, 16]

# Calcular la varianza
varianza = statistics.variance(datos)
print(f"Varianza: {varianza}")

# Calcular la desviación estándar
desviacion_estandar = statistics.stdev(datos)
print(f"Desviación estándar: {desviacion_estandar}")
