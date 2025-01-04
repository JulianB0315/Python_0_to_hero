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
