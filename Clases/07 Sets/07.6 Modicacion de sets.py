#-------------------------------------------------------------------------------------------------------------------------------------------
#Para eliminar un elemento de un conjunto en Python, puedes usar los métodos remove(), discard(), o pop().
#-------------------------------------------------------------------------------------------------------------------------------------------
#remove(elemento): Elimina el elemento especificado. Si el elemento no está presente, se lanza un KeyError.
mi_set = {1, 2, 3, 4}
mi_set.remove(3)
print(mi_set)  # Salida: {1, 2, 4}
# mi_set.remove(5)  # Esto causará un KeyError
#discard(elemento): Elimina el elemento especificado sin lanzar un error si el elemento no está presente.
mi_set = {1, 2, 3, 4}
mi_set.discard(2)
print(mi_set)  # Salida: {1, 3, 4}
mi_set.discard(5)  # No ocurre error, simplemente no se elimina nada
#-------------------------------------------------------------------------------------------------------------------------------------------
#Para borrar un set en Python, puedes usar dos métodos principales
#Usar el método clear()
#Este método vacía el set, pero no elimina el objeto del set en sí.
mi_set = {1, 2, 3, 4}
mi_set.clear()  # Vacía el set
print(mi_set)  # Output: set()
#Usar la palabra clave del
#Esta opción elimina completamente el set de la memoria.
mi_set = {1, 2, 3, 4}
del mi_set  # Elimina el set
# print(mi_set)  # Esto causaría un error porque el set ya no existe
#-------------------------------------------------------------------------------------------------------------------------------------------
#Para convertir un set a una lista en Python, puedes usar la función list(). Aquí tienes un ejemplo:
mi_set = {1, 2, 3, 4}
mi_lista = list(mi_set)  # Convierte el set a lista
print(mi_lista)  # Output: [1, 2, 3, 4]
#-------------------------------------------------------------------------------------------------------------------------------------------
#Usar el método union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set_unido = set1.union(set2)  # Une los dos sets
print(set_unido)  # Output: {1, 2, 3, 4, 5}
#Usar el operador |
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set_unido = set1 | set2  # Une los dos sets
print(set_unido)  # Output: {1, 2, 3, 4, 5}
#-------------------------------------------------------------------------------------------------------------------------------------------
#Encontrar elementos de intersección
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
interseccion = set1.intersection(set2)  # Encuentra la intersección
print(interseccion)  # Output: {3, 4}
#Usar el operador &
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
interseccion = set1 & set2  # Encuentra la intersección
print(interseccion)  # Output: {3, 4}
#-------------------------------------------------------------------------------------------------------------------------------------------
