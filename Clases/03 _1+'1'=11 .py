#-------------------------------------------------------------------------------------------------------------------------------------------
_1='Respuesta 1'
print(_1+'1')
#-------------------------------------------------------------------------------------------------------------------------------------------
#Operadores aritméticos los cuales son :
print('Operadores aritmeticos')
print('Suma')
print(1 + 2)
print('Resta')
print(2 - 1)
print('Multiplicación')
print(2 * 3)
print('División')
print(9 / 3)#Poniendo una solo / la división solo dará decimal si lo necesita 
print(7 / 2)#Como en este caso siendo la operación más exacta  
print(7 // 2)#Poniendo dos veces /  la división no tendrá decimal y será redondeada 
print(10 // 3)
print('Residuos de la división')
print(3 % 2) #Muestra los residuos de una división                         
print('Potencia')
print(3 ** 2)  
#-------------------------------------------------------------------------------------------------------------------------------------------
#Una cosa interesante de los operadores es que podemos usarlos en cadenas de texto(multiplicación,potencia y suma) 
print('Operadores aritmeticos en cadenas de texto')
print('Hola'+str(5))
 # Tambien
print(' Hola '*5)
print(' Hola '*(2**2) )
#En caso de la suma es una remplazo de las comas y en la multiplicación de multiplica el str anterior solo se pueden usar valores de tipo int
print('Funciona '+ 'tambien '+'con '+'cadenas '+'de '+'texto')
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora veamos los operadores comparativos como dice su nombre sirven para comparar variables, datos, etc.
print('Operadores comparativos')
#Usemos variables 
print('Variables de tipo int')
n1=5 
n2=10
print(n1>n2) #mayor que
print(n1<n2) #Menor que
print(n1>=n2) #mayor o igual que
print(n1<=n2) #menor o igual que
print(n1==n2) #igual que
print(n1!=n2) #diferente que
#Al ejecutar el código la consola nos dará true o false, pero ¿Por qué? es por que esta diciendo si tu declaración es verdadera o falsa
#Pero de podra hacer con str
print('Variables de tipo str')
str1='Messi'
str2='Ronaldo'
print(str1>str2) #mayor que
print(str1<str2) #Menor que
print(str1>=str2) #mayor o igual que
print(str1<=str2) #menor o igual que
print(str1==str2) #igual que
print(str1!=str2) #diferente que
#MMM ¿Sera que Ronaldo es mejor que Messi? Mentira los que hace Python es ordenar por orden alfabético no contando caracteres donde la A=1 y la Z=27
#Veamos si es cierto 
print('Variables de tipo str parte 2')
str3='Cristiano'
print(str1>str3) #mayor que
print(str1<str3) #Menor que
print(str1>=str3) #mayor o igual que
print(str1<=str3) #menor o igual que
print(str1==str3) #igual que
print(str1!=str3) #diferente que
#Si quiero comprar la longuitud usa el len() al inicio de la variable o encerrando la cadena de texto
print('Variables de tipo str con len()')
print(len(str1)>len(str2)) #mayor que
print(len('Pablo')>len('Sebastian')) #mayor que
#-------------------------------------------------------------------------------------------------------------------------------------------
# Veamos operadores Logicos
print('Operadores Logicos')
# En caso de and une las dos cosa a que se refiere que si un comparación no se cumple soltar falso veamos algunos ejemplos
#Si los dos cumple
print(str1!=str3 and len('Pablo')!=len('Sebastian')) 
print(str1<str2 and n1!=n2)
#Si solo uno cumple
print(n1>n2 and str1>str3)
print(str1>=str3 and n1>=n2) 

