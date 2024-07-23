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
print('Variables        \t3\t1')
print('Operadores       \t3\t1')
print('Strings          \t3\t1')
print('Este es un símbolo de barra invertida (\\)')
print('En todos los lenguajes de programación comienza con \"¡Hola, mundo!\"') # para escribir una comilla doble dentro de una comilla simple
#-------------------------------------------------------------------------------------------------------------------------------------------
#En Python hay formas para formatear cadenas de textos 
#El operador “%” es utilizado ora formatear un conjunto de variables incluyendo una “tupla”(Una línea de tamaño fijo)
print('Formateo')
nombre01 = 'Diego'
apellido01 = 'Alfonso'
edad = 20
print('Hola soy %s %s y mi edad es de %d años' %(nombre01, apellido01,edad))
print('Hola soy {} {} y mi edad es de {} años'.format(nombre01,apellido01,edad))
print(f'Hola soy {nombre01} {apellido01} y mi edad es de {edad} años')
#%s - Cadena (o cualquier objeto con una representación de cadena, como números)
#%d - Enteros
#%f - Números de punto flotante
#"%.número de dígitosf" - Números de punto flotante con precisión fija
#
radio = 10
pi = 3.14
area = pi * radio ** 2
print('El área del círculo con un radio %d es %.2f.' %(radio, area))#el 2 se uso para poner los dos numeros despues del punto
print('El área del círculo con un radio {} es {}.' .format(radio, area))
print(f'El área del círculo con un radio {radio} es {area}.')
#ahora con list
libreria = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
print('Las siguientes son bibliotecas de Python:%s' %(libreria))
#-------------------------------------------------------------------------------------------------------------------------------------------
#Esta Interpolación de cadenas /f-Strings es de Python 3,6 a mas
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
#-------------------------------------------------------------------------------------------------------------------------------------------
#Desempaquetado de caracteres 
print('Desempaquetado de caracteres')
lenguaje="python"
a,b,c,d,e,f=lenguaje
print(a)#p
print(b)#y
print(c)#t
print(d)#h
print(e)#o
print(f)#n
#ahora veamos la divison
print('Division')
first_letter = lenguaje[0]
print(first_letter)#p
first_letter = lenguaje[1:3]#yt
print(first_letter)#p
first_letter = lenguaje[-1]
print(first_letter)#Con una menos iniciamos desde el final
first_letter = lenguaje[1:]
print(first_letter)#Imprime desde donde le indiques
first_letter = lenguaje[::-1]
print(first_letter)#Pondremos la palabra al reves 
pto = lenguaje[0:6:2] 
print(pto) # Pto 
#-------------------------------------------------------------------------------------------------------------------------------------------
