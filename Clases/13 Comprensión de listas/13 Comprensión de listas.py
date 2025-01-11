# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🎮
# ****🤖Programador:Julian Burga Bracamonte******
# **********************************************
# ****🔒GitHub:https://github.com/JulianB0315 **    
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🏀
#-------------------------------------------------------------------------------------------------------------------------------------------
#Comprensión de Listas
#La comprensión de listas es una manera concisa y elegante de construir listas a partir de secuencias. Es considerablemente más rápida y clara que usar bucles `for` tradicionales.
#Sintaxis:
# [expresion for elemento in iterable if condicion]
#expresion: Operación o valor que será incluido en la lista resultante.
#elemento: Cada elemento del iterable que se recorre.
#iterable: Cualquier objeto iterable como listas, cadenas o rangos.
#condicion: (Opcional) Un filtro que determina si el elemento se incluye en la lista.
#-------------------------------------------------------------------------------------------------------------------------------------------
#Crear una lista de caracteres desde una cadena
language = 'Python'
list_chars = [char for char in language]
print(list_chars)  # Salida: ['P', 'y', 't', 'h', 'o', 'n']
#Generar una lista de números al cuadrado
squares = [i**2 for i in range(11)]
print(squares)  # Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Filtrar números pares
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)  # Salida: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#Aplanar una lista de listas
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for sublist in nested_list for num in sublist]
print(flat_list)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#-------------------------------------------------------------------------------------------------------------------------------------------
#Funciones Lambda
#Las funciones lambda son pequeñas funciones anónimas de una sola línea. Se usan cuando se necesita una función simple para operaciones rápidas.
#Sintaxis:
#lambda parametros: expresion
#parametros: Argumentos de la función.
#expresion: Lo que será evaluado y devuelto como resultado.
#Multiplicar un número por dos
multiply_by_two = lambda x: x * 2
print(multiply_by_two(4))  # Salida: 8
#Elevar un número al cuadrado
square = lambda x: x**2
print(square(5))  # Salida: 25
#Función Lambda con múltiples argumentos
add_three_numbers = lambda a, b, c: a + b + c
print(add_three_numbers(1, 2, 3))  # Salida: 6
#-------------------------------------------------------------------------------------------------------------------------------------------
#Creación de Funciones Lambda
#Las funciones lambda también pueden crearse dinámicamente para realizar operaciones más complejas.
#Función Lambda que eleva un número a una potencia
power_function = lambda x, power: x**power
print(power_function(2, 3))  # Salida: 8
print([power_function(i, 3) for i in range(1, 6)])  # Salida: [1, 8, 27, 64, 125]
#-------------------------------------------------------------------------------------------------------------------------------------------
#Función Lambda dentro de otra función
# Las funciones lambda pueden usarse dentro de otras funciones para crear comportamientos personalizados.
#Generar una función de potencia
def power(base):
     return lambda exponent: base**exponent
square = power(3)(2)  # 3^2
cube = power(2)(3)    # 2^3
print(square)  # Salida: 9
print(cube)    # Salida: 8
#Filtrar números impares y elevarlos al cuadrado
def filter_and_square(numbers):
     return [x**2 for x in numbers if (lambda y: y % 2 != 0)(x)]
numbers = list(range(10))
print(filter_and_square(numbers))  # Salida: [1, 9, 25, 49, 81]