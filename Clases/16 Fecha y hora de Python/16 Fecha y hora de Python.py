# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🎮
# ****🤖Programador:Julian Burga Bracamonte******
# **********************************************
# ****🔒GitHub:https://github.com/JulianB0315 **    
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🏀
#-------------------------------------------------------------------------------------------------------------------------------------------
# 1. Introducción a datetime
# En Python, el módulo datetime proporciona clases para trabajar con fechas y horas.
#  Este módulo es muy útil cuando necesitamos realizar operaciones con fechas, como obtener la fecha y hora actual, 
# formatear fechas, o calcular la diferencia entre dos momentos en el tiempo.
#-------------------------------------------------------------------------------------------------------------------------------------------
# 2. Obteniendo información de la fecha y hora actual
# Para obtener la fecha y hora actuales, usamos la clase datetime del módulo datetime.
from datetime import datetime

# Obtener la fecha y hora actuales
ahora = datetime.now()
print("Fecha y hora actual:", ahora)
# Explicación:
# datetime.now() devuelve un objeto datetime que contiene la fecha y hora actuales.
# El resultado se verá algo como 2025-01-14 13:45:30.123456.
#-------------------------------------------------------------------------------------------------------------------------------------------
# 3. Formateando la fecha con strftime
# A veces necesitamos presentar la fecha en un formato específico. Para esto, usamos el método strftime(), 
# que nos permite formatear la fecha como una cadena.
# Formatear la fecha
fecha_formateada = ahora.strftime("%Y-%m-%d %H:%M:%S")
print("Fecha formateada:", fecha_formateada)
# Explicación:
# %Y: Año con cuatro dígitos (ej. 2025).
# %m: Mes con dos dígitos (ej. 01).
# %d: Día con dos dígitos (ej. 14).
# %H: Hora en formato de 24 horas.
# %M: Minutos.
# %S: Segundos.
#-------------------------------------------------------------------------------------------------------------------------------------------
# 4. Convertir una cadena de texto a una fecha con strptime
# A veces tenemos fechas en forma de cadenas y necesitamos convertirlas a un objeto datetime. Para ello, usamos el método strptime(),
#  que convierte una cadena en un objeto datetime según el formato que le especifiquemos.
# Convertir una cadena de texto a fecha
fecha_str = "2025-01-14 15:30:00"
fecha_convertida = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
print("Fecha convertida:", fecha_convertida)
# Explicación:
# strptime() toma dos argumentos: la cadena de fecha y el formato en que está escrita.
#-------------------------------------------------------------------------------------------------------------------------------------------
# 5. Usando solo la fecha con la clase date
# Si solo necesitas la parte de la fecha (sin la hora), puedes usar la clase date.
# Obtener solo la fecha
solo_fecha = ahora.date()
print("Solo la fecha:", solo_fecha)
# Explicación:
# now.date() devuelve solo la parte de la fecha, sin la hora. El formato será YYYY-MM-DD.
#-------------------------------------------------------------------------------------------------------------------------------------------
# 6. Usando objetos time para representar solo la hora
# De manera similar, si solo necesitas la parte de la hora, puedes usar la clase time.
# Obtener solo la hora
solo_hora = ahora.time()
print("Solo la hora:", solo_hora)
# Explicación:
# now.time() devuelve solo la parte de la hora, en formato HH:MM:SS.mmmmmm.
#-------------------------------------------------------------------------------------------------------------------------------------------
# 7. Calculando la diferencia entre dos puntos en el tiempo
# A veces necesitamos calcular la diferencia entre dos fechas u horas. Esto se puede hacer utilizando timedelta, 
# que representa una diferencia entre dos objetos datetime.
# Calcular la diferencia entre dos fechas
fecha_inicial = datetime(2025, 1, 14, 10, 30)
fecha_final = datetime(2025, 1, 14, 15, 45)
diferencia = fecha_final - fecha_inicial
print("Diferencia de tiempo:", diferencia)
# Explicación:
# La resta de dos objetos datetime da como resultado un objeto timedelta, que muestra la diferencia entre ellos en días, segundos y microsegundos.
#-------------------------------------------------------------------------------------------------------------------------------------------
# Resumen
# datetime.now(): Obtener la fecha y hora actuales.
# strftime(): Formatear un objeto datetime como cadena.
# strptime(): Convertir una cadena de texto a un objeto datetime.
# date(): Obtener solo la fecha (sin hora).
# time(): Obtener solo la hora (sin fecha).
# timedelta: Calcular la diferencia entre dos fechas u horas.