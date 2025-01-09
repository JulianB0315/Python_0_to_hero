## **Ejercicio 1: Números múltiplos de 5**
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

## **Ejercicio 2: Pirámide invertida**

altura = 4
for x in range(altura,0, -1):
    espacios = " " * (altura - x)
    estrellas = "*" * (x * 2 - 1)
    print(espacios + estrellas)

## **Ejercicio 3: Letras de una palabra**
palabra = input("Ingrese una palabra: ")
for indice,letra in enumerate(palabra):
    print(f"La letra {letra} está en la posición {indice + 1}")

## **Ejercicio 4: Suma de números hasta 100**
suma = 0
num = 1
while suma <= 100:
    num += suma
    suma += 1
print(f"La suma de los números es: {num}")

## **Ejercicio 5: Pedir un número positivo**
num = int(input("Ingrese un número positivo: "))
while num <= 0:
    num = int(input("Ingrese un número positivo: "))
print("Número ingresado correctamente")

## **Ejercicio 6: Contar vocales**
string="programación en Python"
conteo_letras = 0
for letras in string:
    if letras in "aeiouáéíóú":
        conteo_letras += 1
print(f"La cantidad de letras en la palabra es: {conteo_letras}")

## **Ejercicio 7: Tabla de multiplicar de un número**
numero_multiplicar = int(input("Ingrese un número para mostrar su tabla de multiplicar del 1 al 10: "))
while numero_multiplicar <= 0 or numero_multiplicar > 10:
    numero_multiplicar = int(input("Ingrese un número para mostrar su tabla de multiplicar del 1 al 10: "))
for i in range(1, 11):
        print(f"{numero_multiplicar} x {i} = {numero_multiplicar * i}")