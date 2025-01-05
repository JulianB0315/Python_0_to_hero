#-------------------------------------------------------------------------------------------------------------------------------------------
#Acceder a los valores
#Puedes acceder a los valores de un diccionario usando la clave correspondiente.
# Ejemplo: Acceder a los valores de un diccionario
persona = {"nombre": "Juan", "edad": 25, "profesión": "Ingeniero"}
print(persona["nombre"])  # Juan
print(persona["edad"])  # 25
print(persona["profesión"])  # Ingeniero
#Si la clave no existe, Python lanzará un KeyError.
# Ejemplo: KeyError
print(persona["ciudad"])  # KeyError: 'ciudad'
#Por otro lado puedes usar el método get() para acceder a los valores de un diccionario.
# Ejemplo: Usar el método get()
print(persona.get("nombre"))  # Juan
print(persona.get("edad"))  # 25
#-------------------------------------------------------------------------------------------------------------------------------------------
#Agregar o actulizar elementos
#Para agregar una nueva clave o actualizar una existente, simplemente asigna un valor al diccionario.
# Ejemplo: Agregar o actualizar elementos
persona ={"nombre":"Ana","edad":30}
#Agregar un nuevo valor clave 
persona["profesión"] = "Ingeniera"

#Actualizar un valor clave existente
persona["edad"] = 31
print(persona)  # {'nombre': 'Ana', 'edad': 31, 'profesión': 'Ingeniera'}
#-------------------------------------------------------------------------------------------------------------------------------------------
#Eliminar elementos
#Elimina un elemento por su clave ,pero si la clave no existe, Python lanzará un KeyError.
#Ejemplo : Usando del 
carro = {"marca": "Toyota", "modelo": "Corolla", "año": 2015}
del carro["año"]
print(carro)  # {'marca': 'Toyota', 'modelo': 'Corolla'}
#Usando pop()
#Elimina un elemento por su clave y devuelve el valor eliminado. Si la clave no existe, Python lanzará un KeyError.
# Ejemplo: Usando pop()
avion = {"marca": "Boeing", "modelo": "747", "año": 1970}
modelo = avion.pop("modelo")
print(avion)  # {'marca': 'Boeing', 'año': 1970}
#Eliminar todos los elementos
#Para eliminar todos los elementos de un diccionario, usa clear().
# Ejemplo: Usar clear()
computadora = {"marca": "Dell", "modelo": "Inspiron", "año": 2018}
computadora.clear()
print(computadora)  # {}
#-------------------------------------------------------------------------------------------------------------------------------------------
#Verificar si una clave existe
#Usa el operador in para comprobar si la clave en el diccionario exista.
# Ejemplo: Verificar si una clave existe
gato = {"nombre": "Tom", "edad": 5}
print("nombre" in gato)  # True
#Otra forma sería usando un if pero como no lo hemos visto no se incluirá en los ejercicios
if "nombre" in gato:
     print("La clave 'nombre' existe")
else:
    print("La clave 'nombre' no existe")
#-------------------------------------------------------------------------------------------------------------------------------------------
panatalon = {"color": "azul", "talla": "M", "precio": 20}
#Obtener claves, valores o pares de clave-valor
#Usando keys()
#Este devuelve un objeto iterable con todas las claves.
# Ejemplo: Usar keys()
claves = panatalon.keys()
#Usando values()
#Este devuelve un objeto iterable con todos los valores.
# Ejemplo: Usar values()
valores = panatalon.values()
#Usando items() Pares clave-valor
#Este devuelve un objeto iterable con todos los pares clave-valor.
# Ejemplo: Usar items()
pares = panatalon.items()
print(claves)  # dict_keys(['color', 'talla', 'precio'])
print(valores)  # dict_values(['azul', 'M', 20])
print(pares)  # dict_items([('color', 'azul'), ('talla', 'M'), ('precio', 20])
#Nota: Los objetos devueltos por keys(), values() e items() no son listas, pero puedes convertirlos en listas usando list().
#-------------------------------------------------------------------------------------------------------------------------------------------
#Combinar o actulizar diccionarios
#Usa el método update() para combinar o actualizar diccionarios.
# Ejemplo: Combinar o actualizar diccionarios
diccionario1 = {"a": 1, "b": 2}
diccionario2 = {"b": 3, "c": 4}
diccionario1.update(diccionario2)
print(diccionario1)  # {'a': 1, 'b': 3, 'c': 4}
#Union en Python 3.9 o superior (| y |=)
# Nota: Esta forma de unir diccionarios solo está disponible en Python 3.9 o superior. 
# Ejemplo: Union en Python 3.9 o superior
jefe = {"nombre": "Juan", "edad": 30}
datos_extras = {"profesión": "Ingeniero", "experiencia": 5}
#Union usando |
nuevo_jefe = jefe | datos_extras
#Actualización usando |=
jefe |= datos_extras
print(jefe)  # {'nombre': 'Juan', 'edad': 30, 'profesión': 'Ingeniero', 'experiencia': 5}
#-------------------------------------------------------------------------------------------------------------------------------------------
#Longitud de un diccionario
#Para obtener la longitud de un diccionario, usa la función len().
# Ejemplo: Longitud de un diccionario
galaxia = {"nombre": "Vía Láctea", "tipo": "espiral", "año": 100000000}
print(len(galaxia))  # 3
#Nota: La longitud de un diccionario es el número de pares clave-valor.
#-------------------------------------------------------------------------------------------------------------------------------------------
#Copiar un diccionario
#Puedes hacer una copia usando el método copy().
# Ejemplo: Copiar un diccionario
persona = {"nombre": "Juan", "edad": 25}
otra_persona = persona.copy()
print(otra_persona)  # {'nombre': 'Juan', 'edad': 25}
#Otra forma de copiar es usando el constructor dict().
# Ejemplo: Copiar un diccionario con dict()
persona = {"nombre": "Juan", "edad": 25}
otra_persona = dict(persona)
print(otra_persona)  # {'nombre': 'Juan', 'edad': 25}
#-------------------------------------------------------------------------------------------------------------------------------------------
#Iterar sobre un diccionario
#Nota: Todavia no hemos visto bucles y no se incluiran en los ejercicios
#Puedes iterar sobre las claves, valores o pares clave-valor de un diccionario.
# Ejemplo: Iterar sobre las claves
persona = {"nombre": "Juan", "edad": 25, "profesión": "Ingeniero"}
for clave in persona:
    print(clave)
# Ejemplo: Iterar sobre los valores
for valor in persona.values():
    print(valor)
# Ejemplo: Iterar sobre los pares clave-valor
for clave, valor in persona.items():
    print(clave, valor)
#--------------------------------------------------------------------------------------------------------------------------------------------