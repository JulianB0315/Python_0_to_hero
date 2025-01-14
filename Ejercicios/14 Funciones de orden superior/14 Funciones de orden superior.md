# Funciones de orden superior

>[!IMPORTANT]
>## Recordatorio:
>1. Los ejercicios se separan por módulos como “Hola mundo” conteniendo de 2 a 4 actividades relacionadas con la clase previamente leída. 
>2. Para mandar tu respuesta recuerda hacer un pull requests el la carpeta del módulo y también mandar el archivo con el formato **"[titulo del modulo] - [Nombre de usuario de GitHub]"**

>[!NOTE]
> ### Actividades
># Ejercicios: Nivel 1
> 1. **Usar bucles `for`:**
> - Usa un bucle `for` para imprimir cada país en una lista `countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway"]`.
> - Usa un bucle `for` para imprimir cada nombre en una lista `names = ["Alice", "Bob", "Charlie", "Diana"]`.
> - Usa un bucle `for` para imprimir cada número en una lista `numbers = [1, 2, 3, 4, 5]`.
># Ejercicios: Nivel 2
> 1. **Usar `map`:**
> - Usa `map` para crear una nueva lista cambiando cada país a mayúsculas en `countries`.
> - Usa `map` para crear una nueva lista cambiando cada número a su cuadrado en `numbers`.
> - Usa `map` para cambiar cada nombre a mayúsculas en `names`.
> 2. **Usar `filter`:**
> - Usa `filter` para filtrar los países que contienen la palabra `'land'` en la lista `countries`.
> - Usa `filter` para filtrar los países con exactamente seis caracteres en `countries`.
> - Usa `filter` para filtrar los países que tienen seis letras o más en `countries`.
> - Usa `filter` para filtrar los países que comienzan con `'E'`.
> 3. **Combinación de iteradores:**
> - Encadena dos o más iteradores de lista, como: `arr.map(callback).filter(callback).reduce(callback)`.
> 4. **Funciones personalizadas:**
> - Declara una función llamada `get_string_lists` que tome una lista como parámetro y devuelva una lista que contenga solo los elementos tipo string.
> - Usa `reduce` para sumar todos los números en `numbers`.
> - Usa `reduce` para concatenar todos los países en la lista `countries` y producir esta oración:  
>   *"Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries."*
> 5. **Manipulación de listas:**
> - Declara una función llamada `categorize_countries` que devuelva una lista de países con un patrón común, por ejemplo: `'land'`, `'ia'`, `'island'`, `'stan'`.
> - Crea una función que devuelva un diccionario donde las claves sean las letras iniciales de los países y los valores sean el número de países que comienzan con esa letra.
> - Declara una función `get_first_ten_countries` que devuelva los primeros diez países de la lista `countries`.
> - Declara una función `get_last_ten_countries` que devuelva los últimos diez países de la lista `countries`.
># Ejercicios: Nivel 3
> 1. **Manipulación de datos de países:**  
>    Usando el archivo `countries_data.py`, realiza las siguientes tareas:
> - Ordena los países por nombre, capital y población.
> - Encuentra los diez idiomas más hablados por ubicación.
> - Encuentra los diez países más poblados.
> 2. **Análisis de datos avanzados:**
> - Usa `map` para calcular la densidad de población (población / área) de cada país y devuelve una lista de diccionarios con los resultados.
> - Usa `filter` para encontrar los países con un área mayor a 1 millón de kilómetros cuadrados.
> - Usa `reduce` para calcular la población total de todos los países.
> 3. **Crea reportes personalizados:**
> - Declara una función que clasifique países por continente basándose en su ubicación.
> - Crea un decorador que registre el tiempo de ejecución de cualquier función que procese los datos de países.
> - Declara una función que encuentre el país con la mayor relación entre población y área.

>[!TIP]
>## Y recuerda: 
># "Si puedes imaginarlo puedes programarlo"