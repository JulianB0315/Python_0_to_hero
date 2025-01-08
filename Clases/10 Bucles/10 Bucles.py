# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🎮
# ****🤖Programador:Julia Burga Bracamonte******
# **********************************************
# ****🔒GitHub:https://github.com/JulianB0315 **    
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🏀
#-------------------------------------------------------------------------------------------------------------------------------------------
#¿Qué es un bucle?
#Un bucle es una herramienta que nos permite ejecutar un conjunto de instrucciones varias veces sin tener que escribir el código repetidamente. 
#Los usamos para automatizar tareas repetitivas, como procesar listas de datos o realizar cálculos hasta que se cumpla cierta condición.
#-------------------------------------------------------------------------------------------------------------------------------------------
#Bucles con for:
#Piensa en el bucle for como una herramienta que te ayuda a recorrer una lista de cosas o realizar una acción un número específico de veces.
#Cómo funciona:
#Imagina que tienes una lista de elementos (como números o palabras).
#El bucle toma cada elemento de la lista, uno por uno, y ejecuta las instrucciones que le indiques.
#Ejemplo:
#Usaremos una lista de frutas y un bucle for para imprimir cada fruta en la lista.
#Sintaxis:
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    print(x)
#Esto es como decir: "Por cada fruta en la lista de frutas, imprímela".
#Otra utilidad es repetir algo un número fijo de veces. Por ejemplo:
for i in range(5):
    print("Hola")
#Esto imprimirá "Hola" 5 veces. Aquí, range(5) genera los números del 0 al 4.
#-------------------------------------------------------------------------------------------------------------------------------------------
#Bucles con while:
#El bucle while se basa en una condición. Mientras la condición sea verdadera (True), el bucle seguirá ejecutándose. 
#Es como una luz verde que te dice "sigue".
#Cómo funciona:
#Define una condición que se evalúa antes de cada repetición.
#Si la condición es verdadera, el código dentro del bucle se ejecuta.
#Si la condición se vuelve falsa, el bucle se detiene.
#Ejemplo:
#Hagamos un bucle while que imprima los números del 0 al 4.
#Sintaxis:
contador = 0
while contador < 5:
    print(contador)
    contador += 1
#Esto imprimirá los números del 0 al 4.
#Nota: Si olvidas incrementar el contador, el bucle se ejecutará para siempre. ¡Cuidado!
#-------------------------------------------------------------------------------------------------------------------------------------------
#Control de los bucles
#A veces, necesitas detener un bucle antes de que termine. Puedes hacerlo con las palabras clave break y continue.
#Break: Detiene el bucle por completo.
#Continue: Detiene la iteración actual y continúa con la siguiente.
#Ejemplo:
#Imprimamos los números del 0 al 4, pero detengámonos si llegamos al 2.
contador = 0
while contador < 5:
    print(contador)
    if contador == 2:
        break
    contador += 1
#Esto imprimirá 0, 1 y 2.
#Ejemplo:
#Imprimamos los números del 0 al 4, pero saltemos el 2.
contador = 0
while contador < 5:
    contador += 1
    if contador == 2:
        continue
    print(contador)
#Esto imprimirá 1, 3, 4 y 5.
#-------------------------------------------------------------------------------------------------------------------------------------------
#Bucles anidados
#Puedes poner un bucle dentro de otro bucle. Esto se llama bucles anidados.
#Ejemplo:
#Imprimamos una tabla de multiplicar del 1 al 5.
for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()
#Esto imprimirá una tabla de multiplicar del 1 al 5.
#Nota: Los bucles anidados pueden ser difíciles de seguir. Asegúrate de entender cómo funcionan antes de usarlos.
#-------------------------------------------------------------------------------------------------------------------------------------------
#¿Cómo decidir entre for y while?
#Usa for cuando sepas exactamente cuántas veces quieres iterar o tengas un conjunto de elementos para recorrer.
#Usa while cuando la cantidad de repeticiones dependa de una condición que puede cambiar durante la ejecución.
#-------------------------------------------------------------------------------------------------------------------------------------------