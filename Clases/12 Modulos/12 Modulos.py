# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🎮
# ****🤖Programador:Julia Burga Bracamonte******
# **********************************************
# ****🔒GitHub:https://github.com/JulianB0315 **    
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🏀
#-------------------------------------------------------------------------------------------------------------------------------------------
# ¿Qué es un módulo?
# Un módulo en Python es un archivo que contiene definiciones de funciones, clases y variables que puedes reutilizar en otros archivos. 
# Su propósito es organizar el código y promover la reutilización.
# Ejemplo de un módulo:
# Un archivo llamado mi_modulo.py con el siguiente contenido:
def saludar(nombre):
    return f"Hola, {nombre}!"
PI = 3.14159
# Puedes usar este módulo en otro archivo para aprovechar sus funciones y variables.
#-------------------------------------------------------------------------------------------------------------------------------------------
# Creación de un módulo
# Paso 1: Crear el archivo del módulo
# Crea un archivo llamado mi_modulo.py con este contenido:
def saludar(nombre):
    return f"Hola, {nombre}!"

def despedir(nombre):
    return f"Adiós, {nombre}!"

PI = 3.14159
# Paso 2: Usar el módulo
# En otro archivo, por ejemplo main.py, puedes importarlo:
import mi_modulo
#-------------------------------------------------------------------------------------------------------------------------------------------
print(mi_modulo.saludar("Juan"))
print(f"El valor de PI es: {mi_modulo.PI}")
# Importación de funciones desde un módulo
# Puedes importar funciones específicas de un módulo:
from mi_modulo import saludar

print(saludar("Ana"))  # No es necesario usar el prefijo mi_modulo.
#-------------------------------------------------------------------------------------------------------------------------------------------
# Importación de funciones y cambio de nombre
# Puedes cambiar el nombre de las funciones o del módulo al importarlo:
from mi_modulo import saludar as saludar_func

print(saludar_func("Carlos"))
# O cambiar el nombre del módulo completo:

import mi_modulo as mm

print(mm.saludar("Laura"))
#-------------------------------------------------------------------------------------------------------------------------------------------
# Importación de módulos integrados
# Python incluye muchos módulos integrados que puedes usar directamente. Aquí exploraremos algunos:
# Módulo os
# El módulo os permite interactuar con el sistema operativo.
import os
# Obtener el directorio actual
print(os.getcwd())
# Crear una nueva carpeta
os.mkdir("nueva_carpeta")
# Módulo sys
# El módulo sys permite interactuar con el intérprete de Python.
import sys
# Ver la versión de Python
print(sys.version)
# Ver rutas donde Python busca módulos
print(sys.path)
# Módulo statistics
# Este módulo ofrece funciones para cálculos estadísticos.
import statistics
datos = [1, 2, 3, 4, 5, 6]
print("Media:", statistics.mean(datos))
print("Mediana:", statistics.median(datos))
# Módulo math
# El módulo math proporciona funciones matemáticas avanzadas.
import math
print("Raíz cuadrada de 16:", math.sqrt(16))
print("Seno de 90°:", math.sin(math.radians(90)))
# Módulo string
# El módulo string contiene constantes y funciones útiles para manejar cadenas.
import string
# Mostrar todas las letras
print(string.ascii_letters)
# Plantilla de cadena
template = string.Template("Hola, $nombre!")
print(template.substitute(nombre="Luis"))
# Módulo random
# El módulo random genera números aleatorios y selecciona elementos al azar.
import random
# Número aleatorio entre 1 y 10
print(random.randint(1, 10))
# Elegir un elemento al azar de una lista
opciones = ["rojo", "azul", "verde"]
print(random.choice(opciones))
#-------------------------------------------------------------------------------------------------------------------------------------------
# Modelos en Frameworks (Django)
# En Django, los modelos representan tablas en una base de datos. Cada clase en un modelo equivale a una tabla, y cada atributo corresponde a una columna.

# Ejemplo en Django:
# from django.db import models

# class Tarea(models.Model):
#     titulo = models.CharField(max_length=200)
#     descripcion = models.TextField()
#     estado = models.CharField(max_length=20, default="Pendiente")

#     def __str__(self):
#         return self.titulo