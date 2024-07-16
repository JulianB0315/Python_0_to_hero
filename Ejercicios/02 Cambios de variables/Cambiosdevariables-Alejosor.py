# 1. Crea una cadena de texto diciendo tu nombre, edad y con alguna afirmación (print)con solo variables (mínimo de 3 tipos de variables).
# Variables
nombre = "Alejandro"
edad = 23
afirmacion = True

# Crear y imprimir la cadena de texto
print(f"Mi nombre es {nombre}, tengo {edad} años y mi afirmación es que me gusta programar es {afirmacion}.\n" )

# 2. Crea tres variables de diferentes tipos de datos y cambia el tipo de dato a “str” comprueba el cambio con un “type”.
# Variables de diferentes tipos cada una
numero = 25
decimal = 3.14
booleano = False

# Cambiamos el tipo de dato a str y comprobamos el cambio con type
numero_str = str(numero)
print(type(numero_str))  # <class 'str'>

decimal_str = str(decimal)
print(type(decimal_str))  # <class 'str'>

booleano_str = str(booleano)
print(type(booleano_str))  # <class 'str'>

# 3. Crea tres variables con datos que usuario o tu puedan ingresar y después muestra las variables con un print. 
# Ingresa datos por el usuario
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
ciudad = input("Ingresa tu ciudad: ")

# Mostramos las variables
print(f"Nombre: {nombre}\n")
print(f"Edad: {edad}\n")
print(f"Ciudad: {ciudad}\n")
