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
print
cadenas='Vamos cuatro clases de Python'
sub_cadena='cl'
print(cadenas.index(sub_cadena)) #Devuelve el índice más bajo de una subcadena, los argumentos adicionales indican el índice inicial y final (predeterminado 0 y longitud de cadena - 1).
#print(cadenas.index(sub_cadena, 14)) # Si no se encuentra la subcadena, aumenta un valorError.