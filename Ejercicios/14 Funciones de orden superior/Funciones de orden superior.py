# Ejercicios: Nivel 1Ejercicios: Nivel 1
# Usa un bucle for para imprimir cada país en una lista countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway"]
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway"]
for country in countries:
    print(country)

# Usa un bucle for para imprimir cada nombre en una lista names = ["Alice", "Bob", "Charlie", "Diana"].
names = ["Alice", "Bob", "Charlie", "Diana"]
for name in names:
    print(name)

#Usa un bucle for para imprimir cada número en una lista numbers = [1, 2, 3, 4, 5].
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

#Ejercicios: Nivel 2
#Usa map para crear una nueva lista cambiando cada país a mayúsculas en countries.
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway"]
countries = list(map(lambda country: country.upper(), countries))
print(countries)

#Usa map para crear una nueva lista cambiando cada número a su cuadrado en numbers.
numbers = [1, 2, 3, 4, 5]
numbers = list(map(lambda number: number**2, numbers))
print(numbers)

#Usa map para cambiar cada nombre a mayúsculas en names.
names = ["Alice", "Bob", "Charlie", "Diana"]
names = list(map(lambda name: name.upper(), names))
print(names)

#Usa filter para filtrar los países que contienen la palabra 'land' en la lista countries.
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway"]
countries = list(filter(lambda country: 'land' in country, countries))
print(countries)

#Usa filter para filtrar los países con exactamente seis caracteres en countries.
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway"]
countries = list(filter(lambda country: len(country) == 6, countries))
print(countries)

# Usa filter para filtrar los países que tienen seis letras o más en countries.
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway"]
countries = list(filter(lambda country: len(country) >= 6, countries))

# Usa filter para filtrar los países que comienzan con 'E'.
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway"]
countries = list(filter(lambda country: country[0] == 'E', countries))
print(countries)

#Encadena dos o más iteradores de lista, como: arr.map(callback).filter(callback).reduce(callback).
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, filter(lambda x: x > 10, map(lambda x: x**2, numbers)))
print(result)

#Declara una función llamada get_string_lists que tome una lista como parámetro y devuelva una lista que contenga solo los elementos tipo string.
def get_string_lists(lst):
    return list(filter(lambda x: type(x) == str, lst))

print(get_string_lists([1, 2, 3, 'a', 'b', 'c']))

# Usa reduce para sumar todos los números en numbers.
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)

#Usa reduce para concatenar todos los países en la lista countries y producir esta oración:
# "Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries.
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway"]
result = reduce(lambda x, y: x + ', ' + y, countries)
print(f"{result} and Iceland are north European countries.")

#Declara una función llamada categorize_countries que devuelva una lista de países con un patrón común, por ejemplo: 'land', 'ia', 'island', 'stan'.
def categorize_countries(countries):
    return list(filter(lambda country: 'land' in country or 'ia' in country or 'island' in country or 'stan' in country, countries))

print(categorize_countries(["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland", "Pakistan"]))

#Crea una función que devuelva un diccionario donde las claves sean las letras iniciales de los países y los valores sean el número de países que comienzan con esa letra.
def count_countries(countries):
    return reduce(lambda x, y: {**x, y[0]: x.get(y[0], 0) + 1}, countries, {})

print(count_countries(["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland", "Pakistan"]))

#Declara una función get_first_ten_countries que devuelva los primeros diez países de la lista countries.
def get_first_ten_countries(countries):
    return countries[:10]

print(get_first_ten_countries(["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland", "Pakistan"]))

#Declara una función get_last_ten_countries que devuelva los últimos diez países de la lista countries.
def get_last_ten_countries(countries):
    return countries[-10:]

print(get_last_ten_countries(["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland", "Pakistan"]))

#Ejercicios: Nivel 3
# 1 Usando el archivo countries_data.py, realiza las siguientes tareas:
# Ordena los países por nombre, capital y población.
from countries_data import countries

def ordenar_paises(paises):
    paises_por_nombre = sorted(paises, key=lambda x: x['name'])
    paises_por_capital = sorted(paises_por_nombre, key=lambda x: x['capital'])
    paises_ordenados = sorted(paises_por_capital, key=lambda x: x['population'])

    for country in paises_ordenados:
        print(f"{country['name']} - {country['capital']} - {country['population']}")

ordenar_paises(countries)
# Encuentra los diez idiomas más hablados por ubicación.
from functools import reduce
def diez_idiomas_mas_hablados(paises):
    idiomas = reduce(lambda x, y: x + y['languages'], paises, [])
    idiomas = reduce(lambda x, y: {**x, y: x.get(y, 0) + 1}, idiomas, {})
    idiomas = sorted(idiomas.items(), key=lambda x: x[1], reverse=True)
    return idiomas[:10]

print(diez_idiomas_mas_hablados(countries))
# Encuentra los diez países más poblados.
def paises_mas_poblados(paises):
    paises = sorted(paises, key=lambda x: x['population'], reverse=True)
    return paises[:10]

print(paises_mas_poblados(countries))

# 2 Análisis de datos avanzados:
# Usa map para calcular la densidad de población (población / área) de cada país y devuelve una lista de diccionarios con los resultados.
def densidad_poblacion(paises):
    # Usamos map para calcular la densidad de población y devolver una nueva lista de diccionarios
    paises_con_densidad = list(map(lambda x: {**x, 'population_density': x['population'] / x['area']}, paises))
    for country in paises_con_densidad:
        print(f"{country['name']} - {country['population_density']}")
densidad_poblacion(countries)
# Usa filter para encontrar los países con un área mayor a 1 millón de kilómetros cuadrados.
def paises_mayor_area(paises):
    paises = list(filter(lambda x: x['area'] > 1000000, paises))
    for country in paises:
        print(f"{country['name']} - {country['area']}")
paises_mayor_area(countries)
# Usa reduce para calcular la población total de todos los países.
def poblacion_total(paises):
    poblacion = reduce(lambda x, y: x + y['population'], paises, 0)
    print(poblacion)
poblacion_total(countries)

# Crea reportes personalizados:
# Declara una función que clasifique países por continente basándose en su ubicación.
def clasificar_paises_por_continente(paises):
    continentes = reduce(lambda x, y: {**x, y['region']: x.get(y['region'], []) + [y['name']]}, paises, {})
    for key, value in continentes.items():
        print(f"{key}: {value}")

clasificar_paises_por_continente(countries)
# Crea un decorador que registre el tiempo de ejecución de cualquier función que procese los datos de países.
from time import time
def tiempo_ejecucion(func):
    def wrapper(*args, **kwargs):
        inicio = time()
        func(*args, **kwargs)
        print(f"Tiempo de ejecución: {time() - inicio}")
    return wrapper
# Declara una función que encuentre el país con la mayor relación entre población y área.
def mayor_relacion_poblacion_area(paises):
    pais = max(paises, key=lambda x: x['population'] / x['area'])
    print(f"{pais['name']} - {pais['population'] / pais['area']}")
mayor_relacion_poblacion_area(countries)
