# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🎮
# ****🤖Programador:Julian Burga Bracamonte******
# **********************************************
# ****🔒GitHub:https://github.com/JulianB0315 **    
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🏀
#-------------------------------------------------------------------------------------------------------------------------------------------
#Un diccionario es una colección desordenada, modificable e indexada. En Python, los diccionarios se escriben con llaves y tienen claves y valores.
# Ejemplo básico
diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "profesión": "Ingeniero"
}

print(diccionario)  # {'nombre': 'Juan', 'edad': 25, 'profesión': 'Ingeniero'}
#Alguna de las características de los diccionarios son:
#Claves únicas: Cada clave debe ser única. Si intentas duplicar una clave, se sobrescribirá el valor anterior.
#Claves inmutables: Solo pueden ser de tipos inmutables como strings, números o tuplas.
#Acceso rápido a los valores: Los valores se acceden usando las claves, no índices.
#-------------------------------------------------------------------------------------------------------------------------------------------
""" Crear un diccionario en python y hay diferentes formas de hacerlo""" 
#Para crea un diccionario vacío, puedes usar {} o tambiem la funcion dict()
# Ejemplo de diccionario vacío
diccionario = {}
print(diccionario)  # {}
# Ejemplo de diccionario vacío con dict()
diccionario = dict() 
print(diccionario)  # {}
#-------------------------------------------------------------------------------------------------------------------------------------------
#Diccionario valores iniciales
#Puedes definir un diccionario con pares clave-valor entre llaves.
# Ejemplo de diccionario con valores iniciales
diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "profesión": "Ingeniero"
}
print(diccionario)  # {'nombre': 'Juan', 'edad': 25, 'profesión': 'Ingeniero'}
#--------------------------------------------------------------------------------------------------------------------------------------------
#Diccionario con dict()
#También puedes usar la función dict() para crear un diccionario con valores iniciales.
# Ejemplo de diccionario con dict()
diccionario = dict(nombre="Juan", edad=25, profesión="Ingeniero")
print(diccionario)  # {'nombre': 'Juan', 'edad': 25, 'profesión': 'Ingeniero'}
#-------------------------------------------------------------------------------------------------------------------------------------------
#Usando listas o tuplas de pares clave-valor
#Puedes construir un diccionario a partir de una lista o tupla de pares clave-valor usando dict().
#Lista de tuplas 
datos = [("nombre", "Juan"), ("edad", 25), ("profesión", "Ingeniero")]
persona = dict(datos)
print(persona)  # {'nombre': 'Juan', 'edad': 25, 'profesión': 'Ingeniero'}

#Tupla de tuplas
datos = (("nombre", "Juan"), ("edad", 25), ("profesión", "Ingeniero"))
persona = dict(datos)
print(persona)  # {'nombre': 'Juan', 'edad': 25, 'profesión': 'Ingeniero'}
#-------------------------------------------------------------------------------------------------------------------------------------------
#Usando la comprensión de diccionarios
#La comprensión de diccionarios te permite crear diccionarios de una forma compacta y eficiente.
#Nota: Todavia no aprendemos bucles y no se incluiran en este en los ejercicios
#Ejemplo: Crear un diccionario con cuadrados de números
cuadrados = {x:x**2 for x in range(1, 6)}
print(cuadrados)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Ejemplo: Convertir una lista en un diccionario
nombres = ["Juan", "María", "Carlos"]
longitudes = {nombre: len(nombre) for nombre in nombres}
print(longitudes)  # {'Juan': 4, 'María': 5, 'Carlos': 6}
#-------------------------------------------------------------------------------------------------------------------------------------------
#Desde dos listas usando zip()
#Si tenemos dos listas relacionadas, podemos combinarlas en un diccionario usando zip().
# Ejemplo: Convertir dos listas en un diccionario
claves = ["nombre", "edad", "profesión"]
valores = ["Juan", 25, "Ingeniero"]
persona = dict(zip(claves, valores))
print(persona)  # {'nombre': 'Juan', 'edad': 25, 'profesión': 'Ingeniero'}
#-------------------------------------------------------------------------------------------------------------------------------------------
#Diccionario con valores predeterminados
#Puedes crear un diccionario con valores predeterminados usando dict.fromkeys().
# Ejemplo: Crear un diccionario con valores predeterminados
claves = ["nombre", "edad", "profesión"]
persona = dict.fromkeys(claves, "desconocido")
print(persona)  # {'nombre': 'desconocido', 'edad': 'desconocido', 'profesión': 'desconocido'}
#-------------------------------------------------------------------------------------------------------------------------------------------