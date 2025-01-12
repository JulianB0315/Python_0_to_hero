# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🎮
# ****🤖Programador:Julian Burga Bracamonte******
# **********************************************
# ****🔒GitHub:https://github.com/JulianB0315 **    
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🏀
#-------------------------------------------------------------------------------------------------------------------------------------------
# 1. Funciones de orden superior (Higher Order Functions)
# Definición:
# Una función de orden superior es aquella que:
# Recibe otra función como argumento.
# Devuelve otra función como resultado.
#  Ejemplo
def saludo():
    return "¡Hola, mundo!"

def ejecuta_funcion(func):
    return func()

print(ejecuta_funcion(saludo))  # Resultado: ¡Hola, mundo!
# Actividad: Escribe una función que reciba otra función como argumento y la ejecute varias veces.
#-------------------------------------------------------------------------------------------------------------------------------------------
# 2. Funciones como parámetros (Function as a Parameter)
#  Ejemplo
def operacion_matematica(operacion, a, b):
    return operacion(a, b)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b
print(operacion_matematica(suma, 5, 3))  # Resultado: 8
print(operacion_matematica(resta, 5, 3))  # Resultado: 2
#  Actividad: Crea una función que reciba otra para calcular el área de un triángulo, un círculo o un cuadrado.
#-------------------------------------------------------------------------------------------------------------------------------------------
# 3. Funciones como valores de retorno (Function as a Return Value)
#  Ejemplo 
def generador_de_operaciones(operacion):
    if operacion == "suma":
        return lambda a, b: a + b
    elif operacion == "multiplicacion":
        return lambda a, b: a * b

operacion = generador_de_operaciones("suma")
print(operacion(10, 5))  # Resultado: 15
#  Actividad: Crea una función que devuelva una función para calcular intereses simples o compuestos.
#-------------------------------------------------------------------------------------------------------------------------------------------
# 4. Closures en Python
#  Definición: Una closure es una función que "recuerda" las variables de su entorno, incluso después de que ese entorno haya terminado.
#  Ejemplo 
def contador():
    cuenta = 0
    def incrementar():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    return incrementar

mi_contador = contador()
print(mi_contador())  # Resultado: 1
print(mi_contador())  # Resultado: 2
#  Actividad: Escribe un closure que permita llevar un registro de la suma acumulada de números.
#-------------------------------------------------------------------------------------------------------------------------------------------
# 5. Decoradores en Python
# A. Creación de decoradores
#  Ejemplo
def decorador(func):
    def envoltura():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return envoltura

@decorador
def decir_hola():
    print("¡Hola!")

decir_hola()
# B. Aplicación de múltiples decoradores
#  Ejemplo 
def decorador1(func):
    def envoltura():
        print("Decorador 1")
        func()
    return envoltura

def decorador2(func):
    def envoltura():
        print("Decorador 2")
        func()
    return envoltura

@decorador1
@decorador2
def funcion():
    print("Función principal")

funcion()
# C. Decoradores con parámetros
#  Ejemplo 
def decorador_con_parametros(prefijo):
    def decorador(func):
        def envoltura(*args, **kwargs):
            print(f"{prefijo}: Antes de ejecutar la función")
            resultado = func(*args, **kwargs)
            print(f"{prefijo}: Después de ejecutar la función")
            return resultado
        return envoltura
    return decorador

@decorador_con_parametros("DEBUG")
def sumar(a, b):
    return a + b

print(sumar(3, 4))
#  Actividad: Crea un decorador que registre en un archivo de texto todas las ejecuciones de una función.
#-------------------------------------------------------------------------------------------------------------------------------------------
# 6. Funciones integradas de orden superior
# A. map
#  Ejemplo:
numeros = [1, 2, 3, 4]
doble = map(lambda x: x * 2, numeros)
print(list(doble))  # Resultado: [2, 4, 6, 8]
# B. filter
#  Ejemplo:
numeros = [1, 2, 3, 4]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Resultado: [2, 4]
# C. reduce
#  Ejemplo:
from functools import reduce
numeros = [1, 2, 3, 4]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # Resultado: 10