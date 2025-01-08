# Dictionaries

>[!IMPORTANT]
>## Recordatorio:
>1. Los ejercicios se separan por módulos como “Hola mundo” conteniendo de 2 a 4 actividades relacionadas con la clase previamente leída. 
>2. Para mandar tu respuesta recuerda hacer un pull requests el la carpeta del módulo y también mandar el archivo con el formato **"[titulo del modulo] - [Nombre de usuario de GitHub]"**

>[!NOTE]
> ## Actividades:
> ## **Ejercicio 1: Determinar si puedes aprender a conducir**
> 1. Solicita al usuario que ingrese su edad con `input()`.
> 2. Si la edad es 18 o más, muestra: **"Eres lo suficientemente mayor para aprender a conducir."**
> 3. Si es menor, calcula cuántos años faltan para tener 18 y muestra: **"Necesitas X años más para aprender a conducir."**
> ## **Ejercicio 2: Comparar edades**
> 1. Define una edad predefinida (por ejemplo, `mi_edad = 25`).
> 2. Solicita al usuario que ingrese su edad con `input()`.
> 3. Compara las edades y muestra:
>    - Si el usuario es mayor, muestra: **"Eres X años mayor que yo."**
>    - Si es menor, muestra: **"Soy X años mayor que tú."**
>    - Si ambas edades son iguales, muestra: **"Tenemos la misma edad."**
> ## **Ejercicio 3: Comparar dos números**
> 1. Solicita al usuario dos números.
> 2. Muestra:
>    - **"A es mayor que B"** si el primer número es mayor.
>    - **"A es menor que B"** si el primer número es menor.
>    - **"A es igual a B"** si ambos números son iguales.
> ## **Ejercicio 4: Calificar estudiantes según sus notas**
> 1. Solicita una puntuación entre 0 y 100 al usuario.
> 2. Asigna calificaciones según este rango:
>    - **80-100:** A
>    - **70-79:** B
>    - **60-69:** C
>    - **50-59:** D
>    - **0-49:** F
> 3. Muestra la calificación correspondiente.
> ## **Ejercicio 5: Determinar la estación del año**
> 1. Solicita al usuario un mes (por ejemplo, **"Septiembre"**).
> 2. Según el mes, muestra la estación:
>    - **Septiembre, Octubre, Noviembre:** Otoño.
>    - **Diciembre, Enero, Febrero:** Invierno.
>    - **Marzo, Abril, Mayo:** Primavera.
>    - **Junio, Julio, Agosto:** Verano.
> ## **Ejercicio 6: Lista de frutas**
> 1. Define una lista: `frutas = ['banana', 'naranja', 'mango', 'limón']`.
> 2. Solicita al usuario que ingrese el nombre de una fruta.
> 3. Si la fruta ya está en la lista, muestra: **"Esa fruta ya existe en la lista."**
> 4. Si no está, agrégala a la lista y muestra la lista actualizada.
> ## **Ejercicio 7: Trabajando con diccionarios**
> Usa el siguiente diccionario:
> ```python
> persona = {
>     'nombre': 'Juan',
>     'apellido': 'Pérez',
>     'edad': 30,
>     'país': 'España',
>     'casado': True,
>     'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
>     'dirección': {
>         'calle': 'Calle Luna',
>         'código_postal': '28001'
>     }
> }
> ```
> 1. **Verificar habilidades:** Si el diccionario tiene la clave `habilidades`, imprime la habilidad en el medio de la lista.
> 2. **Buscar "Python":** Si `habilidades` incluye **"Python"**, muestra: **"Tiene conocimientos de Python."**
> 3. **Evaluar habilidades:**
>    - Si tiene `JavaScript` y `React`, muestra: **"Es un desarrollador frontend."**
>    - Si tiene `Node`, `Python` y `MongoDB`, muestra: **"Es un desarrollador backend."**
>    - Si tiene `React`, `Node` y `MongoDB`, muestra: **"Es un desarrollador fullstack."**
>    - En otro caso, muestra: **"Título desconocido."**
> 4. **Verificar estado civil y país:** Si la persona está casada y vive en España, muestra:
>    ```plaintext
>    Nombre completo: Juan Pérez
>    País: España
>    Estado civil: Casado
>    ```

>[!TIP]
>## Y recuerda: 
># "Si puedes imaginarlo puedes programarlo"