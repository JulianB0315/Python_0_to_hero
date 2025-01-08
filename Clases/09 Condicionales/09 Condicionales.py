# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🎮
# ****🤖Programador:Julia Burga Bracamonte******
# **********************************************
# ****🔒GitHub:https://github.com/JulianB0315 **    
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🏀
#-------------------------------------------------------------------------------------------------------------------------------------------
#Las condiciones son instrucciones que se ejecutan si se cumple una condición o ciertas de condiciones.
#-------------------------------------------------------------------------------------------------------------------------------------------
#Estructura de basica:
#La palabra clave if se usa para ejecutar un bloque 
# de código si una condición es verdadera.
#Sintaxis:
condicion = True
if condicion:
    print("La condición es verdadera")
#EJemplo:
x = 10
y = 20
if x < y:
    print("x es menor que y")
#-------------------------------------------------------------------------------------------------------------------------------------------

#Estructura de if-else:
#La palabra clave else se usa para ejecutar un bloque de 
# código si la condición es falsa.
#Sintaxis:
condicion = False
if condicion:
    print("La condición es verdadera")
else:
    print("La condición es falsa")
#Ejemplo:
x = 10
y = 20
if x > y:
    print("x es mayor que y")
else:
    print("x es menor que y")
#-------------------------------------------------------------------------------------------------------------------------------------------
#Estructura de if-elif-else:
#La palabra clave elif se usa para agregar más condiciones.
#Sintaxis:
condicion1 = False
condicion2 = False
if condicion1:
    print("La condición 1 es verdadera")
elif condicion2:
    print("La condición 2 es verdadera")
else:
    print("Ninguna de las condiciones es verdadera")
#Ejemplo:
x = 10
y = 20
if x > y:
    print("x es mayor que y")
elif x < y:
    print("x es menor que y")
else:
    print("x es igual a y")
#-------------------------------------------------------------------------------------------------------------------------------------------

#Estructura de if anidado:
#Se pueden anidar las condiciones if dentro de otras condiciones if.
#Sintaxis:
condicion1 = False
condicion2 = False
if condicion1:
    if condicion2:
        print("Ambas condiciones son verdaderas")
    else:
        print("Solo la condición 1 es verdadera")
else:
    print("Ninguna de las condiciones es verdadera")
#Ejemplo:
x = 10
y = 20
if x == y:
    print("x es igual a y")
else:
    if x > y:
        print("x es mayor que y")
    else:
        print("x es menor que y")
#-------------------------------------------------------------------------------------------------------------------------------------------

#Estructura de operadores logicos:
#Los operadores lógicos se utilizan para combinar declaraciones condicionales.
#Sintaxis:
# and: Devuelve True si ambas declaraciones son verdaderas.
# or: Devuelve True si al menos una de las declaraciones es verdadera.
# not: Invierte el resultado, devuelve False si el resultado es verdadero.
#Ejemplo:
x = 10
y = 20
z = 30
if x < y and y < z:
    print("Ambas condiciones son verdaderas")
if x < y or y > z:
    print("Al menos una de las condiciones es verdadera")
if not x == y:
    print("La condición es falsa")
#-------------------------------------------------------------------------------------------------------------------------------------------

#Estructura de operadores de comparación:
#Los operadores de comparación se utilizan para comparar dos valores.
#Sintaxis:
# ==: Igual a
# !=: Diferente de
# >: Mayor que
# <: Menor que
# >=: Mayor o igual que
# <=: Menor o igual que
#Ejemplo:
x = 10
y = 20
if x == y:
    print("x es igual a y")
if x != y:
    print("x es diferente de y")
if x > y:
    print("x es mayor que y")
if x < y:
    print("x es menor que y")
if x >= y:
    print("x es mayor o igual que y")
if x <= y:
    print("x es menor o igual que y")
#-------------------------------------------------------------------------------------------------------------------------------------------
#Estructura de operadores de identidad:
#Los operadores de identidad se utilizan para comparar objetos.
#Sintaxis:
# is: Devuelve True si ambas variables son el mismo objeto.
# is not: Devuelve True si ambas variables no son el mismo objeto.
#Ejemplo:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
if x is z:
    print("x y z son el mismo objeto")
if x is not y:
    print("x y y no son el mismo objeto")
if x == y:
    print("x es igual a y")
#-------------------------------------------------------------------------------------------------------------------------------------------
#Estructura de operadores de pertenencia:
#Los operadores de pertenencia se utilizan para probar si un
# secuencia se encuentra en un objeto.
#Sintaxis:
# in: Devuelve True si un valor específico está presente en el objeto.
# not in: Devuelve True si un valor específico no está presente en el objeto.
#Ejemplo:
x = ["apple", "banana"]
if "banana" in x:
    print("Sí, 'banana' está en la lista")
if "orange" not in x:
    print("Sí, 'orange' no está en la lista")
#-------------------------------------------------------------------------------------------------------------------------------------------
#Estructura de operadores de bits:
#Los operadores de bits se utilizan para comparar números enteros.
#Sintaxis:
# &: AND
# |: OR
# ^: XOR
# ~: NOT
# <<: Desplazamiento a la izquierda
# >>: Desplazamiento a la derecha
#Ejemplo:
x = 10
y = 4
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << 2)
print(x >> 2)
#-------------------------------------------------------------------------------------------------------------------------------------------