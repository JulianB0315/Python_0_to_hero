```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🎮
# ****🤖Programador:Julian Burga Bracamonte******
# **********************************************
# ****🔒GitHub:https://github.com/JulianB0315 **    
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🏀
```
# Python Type Errors

En esta clase exploraremos los tipos de errores más comunes en Python, sus causas y cómo manejarlos de manera efectiva.

## Tipos de errores en Python

### 1. **SyntaxError**
Este error ocurre cuando el código tiene un problema de sintaxis y no puede ser interpretado por Python.

#### Ejemplo:
```python
if True
    print("Hola")
```
#### Solución:
Asegúrate de que la sintaxis sea correcta:
```python
if True:
    print("Hola")
```

---

### 2. **NameError**
Se produce cuando se intenta usar una variable o función que no ha sido definida.

#### Ejemplo:
```python
print(nombre)
```
#### Solución:
Define la variable antes de usarla:
```python
nombre = "Juan"
print(nombre)
```

---

### 3. **IndexError**
Ocurre cuando intentas acceder a un índice que no existe en una lista.

#### Ejemplo:
```python
lista = [1, 2, 3]
print(lista[5])
```
#### Solución:
Asegúrate de que el índice esté dentro del rango:
```python
lista = [1, 2, 3]
if len(lista) > 5:
    print(lista[5])
else:
    print("Índice fuera de rango")
```

---

### 4. **ModuleNotFoundError**
Sucede cuando intentas importar un módulo que no está instalado o no existe.

#### Ejemplo:
```python
import mod_inexistente
```
#### Solución:
Instala o corrige el nombre del módulo:
```bash
pip install nombre_modulo
```
O importa el módulo correcto:
```python
import math
```

---

### 5. **AttributeError**
Ocurre cuando intentas acceder a un atributo o método que no existe para un objeto.

#### Ejemplo:
```python
texto = "Hola"
texto.apender("!")
```
#### Solución:
Verifica los métodos disponibles para el objeto:
```python
texto = "Hola"
texto = texto + "!"
print(texto)
```

---

### 6. **KeyError**
Se produce cuando intentas acceder a una clave que no existe en un diccionario.

#### Ejemplo:
```python
diccionario = {"nombre": "Juan"}
print(diccionario["edad"])
```
#### Solución:
Usa el método `get` para proporcionar un valor predeterminado:
```python
diccionario = {"nombre": "Juan"}
print(diccionario.get("edad", "Clave no encontrada"))
```

---

### 7. **TypeError**
Se da cuando realizas una operación entre tipos incompatibles.

#### Ejemplo:
```python
print("Hola" + 5)
```
#### Solución:
Convierte los tipos apropiadamente:
```python
print("Hola" + str(5))
```

---

### 8. **ImportError**
Sucede cuando no se puede importar una función o clase de un módulo.

#### Ejemplo:
```python
from math import raiz
```
#### Solución:
Asegúrate de usar los nombres correctos:
```python
from math import sqrt
```

---

### 9. **ValueError**
Se produce cuando una función recibe un argumento con el tipo correcto pero un valor inapropiado.

#### Ejemplo:
```python
numero = int("Hola")
```
#### Solución:
Verifica los valores antes de convertirlos:
```python
texto = "123"
if texto.isdigit():
    numero = int(texto)
```

---

### 10. **ZeroDivisionError**
Ocurre cuando intentas dividir un número por cero.

#### Ejemplo:
```python
resultado = 10 / 0
```
#### Solución:
Verifica que el divisor no sea cero:
```python
divisor = 0
if divisor != 0:
    resultado = 10 / divisor
else:
    print("No se puede dividir por cero")
```

---

## Resumen
Estos errores son comunes al programar en Python, pero con buenas prácticas y validaciones adecuadas puedes evitarlos y solucionarlos rápidamente. ¡Sigue practicando para mejorar tus habilidades!
