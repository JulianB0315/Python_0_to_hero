#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora aprendamos como agregar elementos los “sets”
#-------------------------------------------------------------------------------------------------------------------------------------------
#Para agregar un elemento a un conjunto en Python, utilizamos el método add(). Este método permite incluir un solo elemento, y si el elemento ya está presente, no se agrega nuevamente.
# Crear un conjunto
mi_set = {1, 2, 3}
# Agregar un elemento
mi_set.add(4)
# Imprimir el conjunto
print(mi_set)  # Salida: {1, 2, 3, 4}
# Agregar un elemento duplicado
mi_set.add(2)
print(mi_set)  # Salida: {1, 2, 3, 4} (sin cambios)
#Para agregar múltiples elementos, utiliza el método update():
mi_set.update([5, 6])
print(mi_set)  # Salida: {1, 2, 3, 4, 5, 6}
