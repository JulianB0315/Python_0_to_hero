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
#Subconjunto (Subset)
#Un conjunto A es un subconjunto de un conjunto B si todos los elementos de A están en B. 
#Para comprobar esto, puedes usar el método issubset() o el operador <=.
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
# Usando el método issubset()
print(A.issubset(B))  # True
# Usando el operador <=
print(A <= B)  # True
#Superconjunto (Superset)
#Un conjunto A es un superconjunto de un conjunto B si todos los elementos de B están en A. 
#Para comprobar esto, puedes usar el método issuperset() o el operador >=.
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
# Usando el método issuperset()
print(A.issuperset(B))  # True
# Usando el operador >=
print(A >= B)  # True
#Subconjunto estricto y superconjunto estricto
#Si quieres verificar si un conjunto A es un subconjunto estricto
#(es decir, si A es subconjunto de B pero no es igual a B) o un superconjunto estricto (es decir, 
#si A es superconjunto de B pero no es igual a B),
#puedes usar los métodos issubset() y issuperset() con la condición de que los conjuntos no sean iguales:
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
# Subconjunto estricto (A es subconjunto de B, pero no es igual a B)
print(A < B)  # True
# Superconjunto estricto (A es superconjunto de B, pero no es igual a B)
print(B > A)  # True
#-------------------------------------------------------------------------------------------------------------------------------------------
#Comprobación de la diferencia entre dos conjuntos
#La diferencia entre dos conjuntos A y B devuelve un nuevo conjunto con los elementos que están en A pero no en B.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# Usando el método difference()
difference_A_B = A.difference(B)
print(difference_A_B)  # {1, 2, 3}
# Usando el operador -
difference_A_B = A - B
print(difference_A_B)  # {1, 2, 3}
#Diferencia simétrica (Elementos en A o B, pero no en ambos):}
#Si deseas encontrar los elementos que están en A o en B, pero no en ambos (es decir, la diferencia simétrica), 
#puedes usar el método symmetric_difference() o el operador ^.
# Usando el método symmetric_difference()
symmetric_difference = A.symmetric_difference(B)
print(symmetric_difference)  # {1, 2, 3, 6, 7, 8}
# Usando el operador ^
symmetric_difference = A ^ B
print(symmetric_difference)  # {1, 2, 3, 6, 7, 8}
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora ya estas list@ para el Modulo "https://github.com/JulianB0315/Python_0_to_hero/blob/main/Ejercicios/07%20Sets/07%20Sets.md"