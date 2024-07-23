print('Funciones')
cadenas = 'vamos cuatro clases de Python'
print(cadenas.capitalize())#Esta función convierte la primera letra en mayúscula 
print(cadenas.count('s')) # Devuelve ocurrencias de subcadena en cadena, count(subcadena, start=.., end=..). 
print(cadenas.count('a', 1, 21)) #El inicio es una indexación inicial para contar y el final es el último índice para contar.
print(cadenas.count('a')) 
print(cadenas.endswith('on'))#Comprueba si una cadena termina con un final especificado
print(cadenas.endswith('tion'))
cadenas = 'vamos\tcuatro\tclases\tde\tPython'
print(cadenas.expandtabs()) #Reemplaza el carácter de pestaña con espacios, el tamaño de pestaña predeterminado es 8. Se necesita un argumento de tamaño de pestaña
print(cadenas.expandtabs(10))
cadenas = 'vamos cuatro clases de Python'
print(cadenas.find('a')) #Devuelve el índice de la primera aparición de una subcadena, si no se encuentra devuelve -1
print(cadenas.find('th')) 
print(cadenas.rfind('y'))#Devuelve el índice de la última aparición de una subcadena, si no se encuentra, devuelve -1
print(cadenas.rfind('th'))