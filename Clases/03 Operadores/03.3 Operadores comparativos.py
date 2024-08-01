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