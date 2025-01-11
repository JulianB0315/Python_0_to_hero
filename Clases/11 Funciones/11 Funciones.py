# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🎮
# ****🤖Programador:Julian Burga Bracamonte******
# **********************************************
# ****🔒GitHub:https://github.com/JulianB0315 **    
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🏀
#-------------------------------------------------------------------------------------------------------------------------------------------
#Definición de una función
#Una función es un bloque de código que se ejecuta solo cuando es llamada. Se define con la palabra clave def.
#Ejemplo:
def ejemplo():
    print("Esta es una función en Python.")
#Esto define una función llamada ejemplo que imprime un mensaje.
#Para ejecutar la función, simplemente llámala:
ejemplo()
#-------------------------------------------------------------------------------------------------------------------------------------------
#Función sin parámetros
#Una función puede no recibir datos de entrada.
#Ejemplo:
def saludo():
    print("Hola, mundo!")
#Llamamos a la función:
saludo()
#-------------------------------------------------------------------------------------------------------------------------------------------
#Función que devuelve un valor
#Se utiliza la palabra clave return para devolver un valor.
#Ejemplo:
def suma(a, b):
    return a + b
#Llamamos a la función y guardamos el resultado en una variable:
resultado = suma(5, 3)
print(resultado)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Función con parámetros
#Las funciones pueden recibir datos como parámetros para personalizar su ejecución.
#Ejemplo:
def saludo(nombre):
    print(f"Hola, {nombre}!")
#Llamamos a la función y pasamos un argumento:
saludo("Julian")
#-------------------------------------------------------------------------------------------------------------------------------------------
#Paso de argumentos con clave y valor
#Se pueden pasar parámetros nombrados (keyword arguments) para mayor claridad.
#Ejemplo:
def saludo(nombre, apellido):
    print(f"Hola, {nombre} {apellido}!")
#Llamamos a la función con argumentos nombrados:
saludo(apellido="Burga", nombre="Julian")
#-------------------------------------------------------------------------------------------------------------------------------------------
#Función con parámetros predeterminados
#Los parámetros predeterminados tienen un valor por defecto si no se proporciona uno al llamar la función.
#Ejemplo:
def saludo(nombre="Invitado"):
    print(f"Hola, {nombre}!")
#Llamamos a la función sin argumentos:
saludo()
saludo("Lucía")
#-------------------------------------------------------------------------------------------------------------------------------------------
#Número arbitrario de argumentos
#Se puede usar *args para aceptar una cantidad indefinida de argumentos.
#Ejemplo:
def saludo(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}!")
#Llamamos a la función con varios argumentos:
saludo("Julian", "Lucía", "Pedro")
#-------------------------------------------------------------------------------------------------------------------------------------------
#Número arbitrario y predeterminado de parámetros
#Se combinan *args y parámetros predeterminados para mayor flexibilidad.
#Ejemplo:
def saludo(*nombres, mensaje="Hola"):
    for nombre in nombres:
        print(f"{mensaje}, {nombre}!")
#Llamamos a la función con varios argumentos y un mensaje personalizado:
saludo("Julian", "Lucía", "Pedro", mensaje="Buen día")
#-------------------------------------------------------------------------------------------------------------------------------------------
#Función como parámetro de otra función
#En Python, las funciones son objetos, por lo que pueden ser pasadas como parámetros.
#Ejemplo:
def saludo():
    return "Hola"
def despedida():
    return "Adiós"
def conversacion(funcion):
    print(funcion())
#Llamamos a la función conversacion y pasamos otra función como argumento:
conversacion(saludo)
conversacion(despedida)
#-------------------------------------------------------------------------------------------------------------------------------------------
# Buenas prácticas
# Dale un nombre descriptivo a tus funciones.
# Documenta las funciones usando cadenas de documentación (""" """).
# Mantén el cuerpo de las funciones limpio y legible.
# Escribe funciones que hagan una sola cosa.
#-------------------------------------------------------------------------------------------------------------------------------------------