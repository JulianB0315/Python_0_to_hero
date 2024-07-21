#El texto es un tipo de datos de cadena. Cualquier tipo de datos escrito como texto es una cadena. 
#Cualquier dato bajo cotización simple, doble o triple son cadenas.
#Existen diferentes métodos de cadena y funciones integradas para tratar los tipos de datos de cadena.
#Para verificar la longitud de una cadena, use el método len().
#Creamos una variable
string="A"
print(string)#Imprime solo el valor de variable, pero agregando la función len()  se usa para contar las letras de str
print(len(string))
string_02= 'Hola mundoooo!'  # No solo te limites a una letra crea tu oración 
print(string_02)             # Hola mundooo!
print(len(string_02))
string_03="Aprendemos python de una manera fácil"
print(string_03)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Podemos usar las comillas para pone nuestra cadena de texto en varias líneas
multi_string='''Python es demasiado fácil de
aprender en este repositorio, 
actualizamos los ficheros cada semana'''
print(multi_string)
#Con las comillas dobles es igual
multi_string="""Python es demasiado fácil de
aprender en este repositorio, 
actualizamos los ficheros cada semana"""
print(multi_string)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Podemos conectar cadenas de texto
Nombre = 'Pablo'
Apellido = 'Escobar'
Espacio = ' '
nombre_completo = Nombre+Espacio+ Apellido#Pablo Escobar
print(nombre_completo) 
print(len(Nombre))
print(len(Apellido))   
print(len(Nombre) > len(Apellido)) 
print(len(nombre_completo))
#-------------------------------------------------------------------------------------------------------------------------------------------
#En Python y otros lenguajes de programación \ seguido de un carácter es una secuencia de escape
print('Es fácil aprender Python.\n¿Lo estas entendiendo?')#\n: nueva línea
print('Clases\tTemas\tModulos')#\t: Tab significa(8 espacios)
print('print(Hola mundo)\t1\t1')
print('Day 2\t3\t1')
print('Day 3\t\t1')
print('Day 4\t1\t1')