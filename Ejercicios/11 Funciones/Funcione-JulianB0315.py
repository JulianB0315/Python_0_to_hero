# 1 Suma de dos número
def suma_dos_numeros(a, b):
    return a + b
resultado = suma_dos_numeros(3, 4)
print(resultado)

# 2 Área de un círculo
def area_circulo(radio):
    return 3.14159 * radio ** 2
resultado = area_circulo(6)
print(resultado)

# 3 Suma de argumentos arbitrarios
def sumar_todo(*args):
    suma = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return f"Error: '{arg}' no es un número válido."
        suma += arg
    return suma
print(sumar_todo(1, 2, 3, 4))
print(sumar_todo(1, 'a', 3))
# 4 Convertir temperatura
def convertir_celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32
resultado = convertir_celsius_a_fahrenheit(100)
print(resultado)

# 5 Estaciones del año
def determinar_estacion(mes):
    if mes in (1, 2, 12):
        return 'Invierno'
    elif mes in (3, 4, 5):
        return 'Primavera'
    elif mes in (6, 7, 8):
        return 'Verano'
    elif mes in (9, 10, 11):
        return 'Otoño'
    else:
        return 'Mes no válido'
resultado = determinar_estacion(5)
print(resultado)

# 6 Imprimir elementos de una lista
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)
imprimir_lista([1, 2, 3, 4, 5])

# 7 Lista invertida
def invertir_lista(lista):
    return lista[::-1]
resultado = invertir_lista([1, 2, 3, 4, 5])
print(resultado)

# 8 Capitalizar elementos de una lista
def capitalizar_lista(lista):
    return [elemento.capitalize() for elemento in lista] 
resultado = capitalizar_lista(['hola', 'mundo'])
print(resultado)

# 9 Agregar un elemento a una lista
def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista
resultado = agregar_elemento([1, 2, 3, 4, 5], 6)
print(resultado)

# 10 Eliminar un elemento de una lista
def eliminar_elemento(lista,elemento):
    lista.remove(elemento)
    return lista
resultado = eliminar_elemento([1, 2, 3, 4, 5], 3)
print(resultado)

# 11 Suma de un rango de números
def suma_de_numeros(n):
    return sum(range(n + 1))
resultado = suma_de_numeros(10)
print(resultado)

# 12 Suma de números impares
def suma_de_impares(n):
    return sum(range(1, n + 1, 2))
resultado = suma_de_impares(10)
print(resultado)

# 13 Suma de números pares
def suma_de_pares(n):
    return sum(range(0, n + 1, 2))
resultado = suma_de_pares(10)
print(resultado)

# 14 Contar pares e impares
def contar_pares_e_impares(n):
    pares = len(range(0, n + 1, 2))
    impares = len(range(1, n + 1, 2))
    return pares, impares
resultado = contar_pares_e_impares(10)
print(resultado)

# 15 Factorial de un número
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
resultado = factorial(5)
print(resultado)

# 16 Verificar si una lista está vacía
def lista_vacia(lista):
    return len(lista) == 0
resultado = lista_vacia([])
print(resultado)

# 17 Calcular estadísticas de una lista
def calcular_estadisticas(lista):
    return {
        'media': sum(lista) / len(lista),
        'mediana': lista[len(lista) // 2],
        'moda': max(set(lista), key = lista.count),
        'rango': max(lista) - min(lista),
        'varianza': sum((x - sum(lista) / len(lista)) ** 2 for x in lista) / len(lista),
        'desviación estándar': (sum((x - sum(lista) / len(lista)) ** 2 for x in lista) / len(lista)) ** 0.5
    }
resultado = calcular_estadisticas([1, 2, 3, 4, 5])
print(resultado)

# 18 Número primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
resultado = es_primo(7)
print(resultado)

# 19 Verificar elementos únicos
def elementos_unicos(lista):
    return len(lista) == len(set(lista))
resultado = elementos_unicos([1, 2, 3, 4, 5])
print(resultado)

# 20 Verificar tipos de datos
def verificar_tipos(*args):
    return [type(arg) for arg in args]
resultado = verificar_tipos(1, 'a', 3.0)
print(resultado)

# 21 Variable válida en Python
import keyword

def variable_valida(nombre):
    # Verificar si el nombre está vacío
    if not nombre:
        return False
    if nombre in keyword.kwlist:
        return False
    if not nombre.isidentifier():
        return False
    return True
resultado = variable_valida('hola')
print(resultado)

# 22 Idiomas más hablados
def idiomas_mas_hablados():
    return {
        'Chino mandarín': 918000000,
        'Español': 460000000,
        'Inglés': 379000000,
        'Hindi': 341000000,
        'Árabe': 319000000,
        'Bengalí': 228000000,
        'Portugués': 221000000,
        'Ruso': 154000000,
        'Japonés': 128000000,
        'Lahnda': 119000000
    }
resultado = idiomas_mas_hablados()
print(resultado)

# 23 Países más poblados
def paises_mas_poblados():
    return {
        'China': 1439323776,
        'India': 1380004385,
        'Estados Unidos': 331002651,
        'Indonesia': 273523615,
        'Pakistán': 220892340,
        'Brasil': 212559417,
        'Nigeria': 206139587,
        'Bangladés': 164689383,
        'Rusia': 145934462,
        'México': 128932753
    }
resultado = paises_mas_poblados()
print(resultado)
