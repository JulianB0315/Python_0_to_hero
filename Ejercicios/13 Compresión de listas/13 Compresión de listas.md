# Modulos

>[!IMPORTANT]
>## Recordatorio:
>1. Los ejercicios se separan por módulos como “Hola mundo” conteniendo de 2 a 4 actividades relacionadas con la clase previamente leída. 
>2. Para mandar tu respuesta recuerda hacer un pull requests el la carpeta del módulo y también mandar el archivo con el formato **"[titulo del modulo] - [Nombre de usuario de GitHub]"**

>[!NOTE]
> ### Actividades
>
> 1. **Filtrar solo los números positivos de la lista usando comprensión de listas:**
>
>    ```python
>    numeros = [-10, -5, 0, 5, 10, 15, -20]
>    # Resultado esperado: [5, 10, 15]
>    ```
>
> 2. **Aplanar la siguiente lista de listas en una lista unidimensional:**
>
>    ```python
>    lista_anidada = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
>    # Resultado esperado: [1, 2, 3, 4, 5, 6, 7, 8]
>    ```
>
> 3. **Crear una lista de potencias de un número:**
>
>    ```python
>    # Genera una lista de potencias del 2 desde 2^0 hasta 2^10
>    # Resultado esperado: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
>    ```
>
> 4. **Convertir las siguientes listas de países y ciudades a un formato personalizado:**
>
>    ```python
>    paises = [[('Perú', 'Lima')], [('Chile', 'Santiago')], [('Colombia', 'Bogotá')]]
>    # Resultado esperado: [['PERÚ', 'PER', 'LIMA'], ['CHILE', 'CHI', 'SANTIAGO'], ['COLOMBIA', 'COL', 'BOGOTÁ']]
>    ```
>
> 5. **Transformar las listas de países a un diccionario:**
>
>    ```python
>    paises = [[('Perú', 'Lima')], [('Chile', 'Santiago')], [('Colombia', 'Bogotá')]]
>    # Resultado esperado:
>    # [{'pais': 'PERÚ', 'ciudad': 'LIMA'},
>    #  {'pais': 'CHILE', 'ciudad': 'SANTIAGO'},
>    #  {'pais': 'COLOMBIA', 'ciudad': 'BOGOTÁ'}]
>    ```
>
> 6. **Concatenar nombres y apellidos en una lista de cadenas:**
>
>    ```python
>    nombres = [[('Luis', 'Martínez')], [('Ana', 'García')], [('José', 'Pérez')]]
>    # Resultado esperado: ['Luis Martínez', 'Ana García', 'José Pérez']
>    ```
>
> 7. **Escribir una función lambda para calcular la pendiente o la intersección en el eje \( y \) de una función lineal:**
>
>    La ecuación de una recta es \( y = mx + b \). Escribe una función lambda para:
>
>    - Calcular la **pendiente** \( m \) dada la ecuación de dos puntos \((x1, y1)\) y \((x2, y2)\).
>    - Calcular la **intersección en el eje y** \( b \) usando la ecuación \( b = y - mx \).
>
>    ```python
>    # Fórmulas:
>    # pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
>    # intersección = lambda x, y, m: y - m * x
>
>    # Prueba con puntos (2, 3) y (5, 11)
>    # Resultado esperado: pendiente = 2.666..., intersección = -2.333...
>    ```

>[!TIP]
>## Y recuerda: 
># "Si puedes imaginarlo puedes programarlo"