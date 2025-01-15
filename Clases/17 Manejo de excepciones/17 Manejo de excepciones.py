# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🎮
# ****🤖Programador:Julian Burga Bracamonte******
# **********************************************
# ****🔒GitHub:https://github.com/JulianB0315 **    
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🏀
#-------------------------------------------------------------------------------------------------------------------------------------------
# 1. Manejo de Excepciones en Python
# El manejo de excepciones permite gestionar errores de manera controlada para que no detengan la ejecución de un programa.
# Estructura básica:
try:
    # Bloque donde podría ocurrir una excepción
    resultado = 10 / 0
except ZeroDivisionError as e:
    # Manejo de la excepción
    print(f"Error: {e}")
else:
    # Si no ocurre ninguna excepción
    print(f"Resultado: {resultado}")
finally:
    # Este bloque siempre se ejecuta
    print("Ejecución finalizada.")
#-------------------------------------------------------------------------------------------------------------------------------------------
# Tipos comunes de excepciones:
# ZeroDivisionError: División entre cero.
# ValueError: Valor inválido.
# TypeError: Tipo de dato incorrecto.
# FileNotFoundError: Archivo no encontrado.
#-------------------------------------------------------------------------------------------------------------------------------------------
# Crear excepciones personalizadas:
class MiExcepcion(Exception):
    pass
try:
    raise MiExcepcion("Este es un error personalizado.")
except MiExcepcion as e:
    print(f"Capturado: {e}")
#-------------------------------------------------------------------------------------------------------------------------------------------
# 2. Empaquetado y Desempaquetado de Argumentos
# Desempaquetado
# El desempaquetado permite extraer elementos de listas, tuplas o diccionarios de manera sencilla.
# Desempaquetado de listas y tuplas:
numeros = [1, 2, 3]
a, b, c = numeros
print(a, b, c)  # Salida: 1 2 3
# Uso de asterisco para capturar el resto:
valores = [1, 2, 3, 4, 5]
a, *b, c = valores
print(a, b, c)  # Salida: 1 [2, 3, 4] 5
# Desempaquetado de diccionarios:
datos = {"nombre": "Ana", "edad": 25}
clave1, clave2 = datos
print(clave1, clave2)  # Salida: nombre edad
# # Desempaquetado de valores:
print(*datos.values())  # Salida: Ana 25
#-------------------------------------------------------------------------------------------------------------------------------------------
# Empaquetado
# El empaquetado permite agrupar elementos en una lista, tupla o diccionario
#-------------------------------------------------------------------------------------------------------------------------------------------
# Empaquetado de listas y tuplas:
def empaquetar(*args):
    print(args)
empaquetar(1, 2, 3, 4)  # Salida: (1, 2, 3, 4)
#-------------------------------------------------------------------------------------------------------------------------------------------
# Empaquetado de diccionarios:
def empaquetar_diccionario(**kwargs):
    print(kwargs)
empaquetar_diccionario(nombre="Luis", edad=30)  # Salida: {'nombre': 'Luis', 'edad': 30}
#-------------------------------------------------------------------------------------------------------------------------------------------
# 3. Propagación en Python
# La propagación ocurre cuando una excepción no es manejada en un nivel y se pasa al nivel superior.
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b
def calcular():
    try:
        print(dividir(10, 0))
    except ValueError as e:
        print(f"Error propagado: {e}")
calcular()  # Salida: Error propagado: No se puede dividir entre cero.
#-------------------------------------------------------------------------------------------------------------------------------------------
# 4. Enumerar y Zip
# Enumerar:
frutas = ["manzana", "pera", "uva"]
for indice, fruta in enumerate(frutas):
    print(indice, fruta)
# Salida:
# 0 manzana
# 1 pera
# 2 uva
# La función enumerate agrega índices a los elementos de una lista o iterable.
nombres = ["Ana", "Luis", "Sofía"]
edades = [25, 30, 22]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")
# Salida:
# Ana tiene 25 años.
# Luis tiene 30 años.
# Sofía tiene 22 años.
#-------------------------------------------------------------------------------------------------------------------------------------------
