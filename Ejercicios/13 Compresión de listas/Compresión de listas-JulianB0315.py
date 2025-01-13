#1 Filtrar solo los números positivos de la lista usando comprensión de listas:
numeros = [-10, -5, 0, 5, 10, 15, -20]
positivos = [numero for numero in numeros if numero > 0]
print(positivos)

#2 Aplanar la siguiente lista de listas en una lista unidimensional:
lista_anidada = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
lista_aplanada = [numero for sublista in lista_anidada for lista in sublista for numero in lista]
print(lista_aplanada)

#3 Crear una lista de potencias de un número:
base = 2
potencias = [base ** i for i in range(11)]
print(potencias)

#4 Convertir las siguientes listas de países y ciudades a un formato personalizado:
paises = [[('Perú', 'Lima')], [('Chile', 'Santiago')], [('Colombia', 'Bogotá')]]
paises_personalizado = [[pais[0][0].upper(), pais[0][0][:3].upper(), pais[0][1].upper()]for pais in paises]
print(paises_personalizado)

#5 Transformar las listas de países a un diccionario:
paises = [[('Perú', 'Lima')], [('Chile', 'Santiago')], [('Colombia', 'Bogotá')]]
paises_dict = [{'pais': pais[0][0].upper(), 'ciudad': pais[0][1].upper()} for pais in paises]
print(paises_dict)

#6 Concatenar nombres y apellidos en una lista de cadenas:
nombres = [[('Luis', 'Martínez')], [('Ana', 'García')], [('José', 'Pérez')]]
nombres_completos = [f'{nombre[0][0]} {nombre[0][1]}' for nombre in nombres]
print(nombres_completos)

#7 Escribir una función lambda para calcular la pendiente o la intersección en el eje ( y ) de una función lineal:
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
interseccion = lambda x, y, m: y - m * x
x1, y1 = 2, 3
x2, y2 = 5, 11
m = pendiente(x1, y1, x2, y2)
print(f"Pendiente (m): {m}")
b = interseccion(x1, y1, m)
print(f"Intersección en el eje y (b): {b}")