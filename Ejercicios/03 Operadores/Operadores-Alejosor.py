# Calculadora básica
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
if b != 0:
    print(f"División: {a / b}")
else:
    print("Error: División por cero")

# Multiplicar una cadena de texto
cadena = input("Introduce una cadena de texto: ")
n = int(input("Introduce un número para multiplicar la cadena: "))
print(f"Resultado: {(cadena + " ") * n}")



