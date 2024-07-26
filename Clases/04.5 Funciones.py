#Ahora veamos una poco de las funciones que nos da Python con los strings
#-------------------------------------------------------------------------------------------------------------------------------------------
print('Funciones')
print('capitalize')
cadenas = 'vamos cuatro clases de Python'
print(cadenas.capitalize())#Esta función convierte la primera letra en mayúscula 
print('count')
print(cadenas.count('s')) # Devuelve ocurrencias de subcadena en cadena, count(subcadena, start=.., end=..). 
print(cadenas.count('a', 1, 21)) #El inicio es una indexación inicial para contar y el final es el último índice para contar.
print(cadenas.count('a'))
print('endswith') 
print(cadenas.endswith('on'))#Comprueba si una cadena termina con un final especificado
print(cadenas.endswith('tion'))
cadenas = 'vamos\tcuatro\tclases\tde\tPython'
print('expandtabs')
print(cadenas.expandtabs()) #Reemplaza el carácter de pestaña con espacios, el tamaño de pestaña predeterminado es 8. Se necesita un argumento de tamaño de pestaña
print(cadenas.expandtabs(10))
print('find y rfind')
cadenas = 'vamos cuatro clases de Python'
print(cadenas.find('a')) #Devuelve el índice de la primera aparición de una subcadena, si no se encuentra devuelve -1
print(cadenas.find('th')) 
print(cadenas.rfind('y'))#Devuelve el índice de la última aparición de una subcadena, si no se encuentra, devuelve -1
print(cadenas.rfind('th'))
print('index')
cadenas='Vamos cuatro clases de Python'
sub_cadena='cl'
print(cadenas.index(sub_cadena)) #Devuelve el índice más bajo de una subcadena, los argumentos adicionales indican el índice inicial y final (predeterminado 0 y longitud de cadena - 1).
#print(cadenas.index(sub_cadena, 14)) # Si no se encuentra la subcadena, aumenta un valorError.
print(cadenas.rindex(sub_cadena))#Devuelve el índice más alto de una subcadena
#print(cadenas.rindex(sub_cadena, 14))#los argumentos adicionales indican el índice inicial y final (el valor predeterminado es 0 y la longitud de la cadena es 1)
print('isdecimal')#Esta función comprueba los números soltando true si hay alguno
n1='30'
print(n1.isdecimal())#true
n2='39.5'
print(n2.isdecimal())#falses
n3='378 abc'
print(n3.isdecimal())#falses
n4='1+2'
print(n4.isdecimal())#falses
print('isdigit')#Comprueba si todos los caracteres de una cadena son números (0-9 y algunos otros caracteres unicode para números)
print(n1.isdigit())#true
print(n2.isdigit())#falses
print(n3.isdigit())#falses
print(n4.isdigit())#falses
print('isnumeric')#Comprueba si todos los caracteres de una cadena están relacionados con números o números (al igual que isdigit(), solo acepta más símbolos, como ½)
print(n1.isnumeric())
print(n2.isnumeric())
print(n3.isnumeric())
print('isidentifier')
cadenas='Vamos cuatro clases de Python'
print(cadenas.isidentifier())# Comprueba un identificador válido: comprueba si una cadena es un nombre de variable válido
cadenas='Vamos_cuatro_clases_de_Python'
print(cadenas.isidentifier())
print('islower')#Comprueba si todos los caracteres del alfabeto en la cadena están en minúsculas
cadenas='vamos cuatro clases de python'
print(cadenas.islower())
cadenas='Vamos cuatro clases de Python'
print(cadenas.islower())
print('isupper')
cadenas='vamos cuatro clases de python'
print(cadenas.isupper())
cadenas='VAMOS CUATRO CLASES DE PYTHON'
print(cadenas.isupper())
print('join')#Devuelve una cadena concatenada
web= ['HTML', 'CSS', 'JavaScript', 'React']
resultado = ' '.join(web)
print(resultado)
resultado = ','.join(web)
print(resultado)
print('strip')#Elimina todos los caracteres dados a partir del principio y el final de la cadena
cadenas='vamos cuatro clases de pythonnnnnnnnnnnnnnnn'
print(cadenas.strip('noth'))
print('replace')
cadenas='Vamos cuatro clases de python'
print(cadenas.replace('python','codigos'))
print('split')#Divide la cadena, usando una cadena o espacio dado como separador
print(cadenas.split())
print('title')#Devuelve una cadena de título en caja
print(cadenas.title())
print('swapcase')# Convierte todos los caracteres en mayúsculas a minúsculas y todos los caracteres en minúsculas a caracteres en mayúsculas
cadenas='vamos cuatro clases de python'
print(cadenas.swapcase())
cadenas='Vamos Cuatro Clases De Python'
print(cadenas.swapcase())
cadenas='cuatro clases de Python'
print('startswith')#Comprueba si la Cadena Comienza con la Cadena Especificada
print(cadenas.startswith('cuatro'))
cadenas='4 clases de Python'
print(cadenas.startswith('cuatro'))
#-------------------------------------------------------------------------------------------------------------------------------------------