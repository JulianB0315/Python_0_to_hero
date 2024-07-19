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
multi_string='''Python es demasiado fácil de
aprender en este repositorio, 
actualizamos los ficheros cada semana'''
print(multi_string)
Nombre = 'Pablo'
Apellido = 'Escobar'
space = ' '
full_name = Nombre +  space + Apellido
print(full_name) 
print(len(Nombre))  
print(len(Apellido))   
print(len(Nombre) > len(Apellido)) 
print(len(full_name)) 