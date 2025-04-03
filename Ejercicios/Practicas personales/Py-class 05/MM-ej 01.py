import statistics

# Ejemplo de cálculo de la media
numeros = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)
print(f"La media es: {media}")

# Alternativa usando el módulo statistics
media_alt = statistics.mean(numeros)
print(f"La media (usando statistics) es: {media_alt}")

# Ejemplo de cálculo de la mediana
numeros2 = [10, 20, 30, 40, 50]
mediana = statistics.median(numeros2)
print(f"La mediana es: {mediana}")
