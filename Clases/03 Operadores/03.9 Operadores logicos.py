#-------------------------------------------------------------------------------------------------------------------------------------------
# Veamos operadores Logicos
print('Operadores Logicos')
# En caso de and une las dos cosa a que se refiere que si un comparación no se cumple soltar falso veamos algunos ejemplos
#Si los dos cumple
str1='Messi'
str2='Ronaldo'
str3='Cristiano'
n1=5 
n2=10
print('Operador and')
print(str1!=str3 and len('Pablo')!=len('Sebastian')) 
print(str1<str2 and n1!=n2)
#Si solo uno cumple
print(n1>n2 and str1>str3)
print(str1>=str3 and n1>=n2) 
#En caso de or una de las dos comparaciones debe de ser verdad
print('Operador or')
print(str1!=str3 and len('Pablo')!=len('Sebastian')) 
print(str1<str2 and n1!=n2)
print(n1>n2 and str1>str3)
print(str1>=str3 and n1>=n2)
#El not es un poco más complicado 
#Pero no imposible este lo que hace es dar true su la comparación no se cumple de lo que este en parentesis
print('Operador not')
print(not(str1<str3))
print(not(str1==str3))
print(not(str1>str3))
print(not(str1!=str3))
#Y con esto terminamos nota: vimos la lógica Boolena te recomiendo verla y estudiarla es una base de para todos los lenguajes de programación 
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora ya estas list@ para el Modulo "Operadores"https://github.com/JulianB0315/Python_0_to_hero/blob/main/Ejercicios/03%20Operadores/03%20Operadores.md