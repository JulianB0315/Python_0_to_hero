import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import bot_biblioteca as bot

# Cargar datos
df_libros = pd.read_csv('Ejercicios/Practicas personales/Py-class 03/libros.csv')
df_usuarios = pd.read_csv('Ejercicios/Practicas personales/Py-class 03/usuarios.csv')

def iniciar_sesion():
    print("Iniciar sesión")
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuario in df_usuarios['usuario'].values:
        if df_usuarios.loc[df_usuarios['usuario'] == usuario, 'contrasena'].values[0] == contrasena:
            print("Inicio de sesión exitoso")
            menu()
        else:
            print("Contraseña incorrecta")
            inicio()
    else:
        print("Usuario no registrado")
        inicio()

def registrarse():
    print("Registrarse")
    usuario = input("Ingrese su usuario: ")
    if usuario in df_usuarios['usuario'].values:
        print("Usuario ya registrado")
        inicio()
    else:
        contrasena = input("Ingrese su contraseña: ")
        df_usuarios.loc[len(df_usuarios)] = [usuario, contrasena]
        df_usuarios.to_csv('Ejercicios/Practicas personales/Py-class 03/usuarios.csv', index=False)
        print("Usuario registrado")
        menu()

def inicio():
    print("Bienvenido a la biblioteca pública")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input()
    if opcion == "1":
        iniciar_sesion()
    elif opcion == "2":
        registrarse()
    elif opcion == "3":
        print("Gracias por visitarnos")
    else:
        print("Opción inválida")
        inicio()

def menu():
    print("\nMenú de la biblioteca")
    print("1. Ver libros")
    print("2. Vender libro")
    print("3. Prestar libro")
    print("4. Buscar libro")
    print("5. Hablar con el bot")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        ver_libros()
    elif opcion == "2":
        vender_libro()
    elif opcion == "3":
        prestar_libro()
    elif opcion == "4":
        buscar_libro()
    elif opcion == "5":
        print("Bot: " + bot.get_response(input("You: ")))
    elif opcion == "6":
        print("Gracias por usar la biblioteca")
        if input("¿Desea guardar los cambios? (si/no): ").strip().lower() == "si":
            df_libros.to_csv('Ejercicios/Practicas personales/Py-class 03/libros.csv', index=False)
            print("Cambios guardados. Que tenga un buen día")
        else:
            print("Cambios no guardados")
    else:
        print("Opción inválida")
        menu()

def ver_libros():
    print("1. Ver todos los libros")
    print("2. Ver libros disponibles")
    print("3. Ver libros vendidos")
    print("4. Ver libros prestados")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(df_libros)
        df_libros['estado'].value_counts().plot(kind='bar', title='Estados de los libros')
        plt.show()
    elif opcion == "2":
        print(df_libros[df_libros['estado'] == 'disponible'])
    elif opcion == "3":
        print(df_libros[df_libros['estado'] == 'vendido'])
    elif opcion == "4":
        print(df_libros[df_libros['estado'] == 'prestado'])
    else:
        print("Opción inválida")
    
    menu()

def vender_libro():
    titulo = input("Ingrese el título del libro a vender: ").strip().lower()

    if titulo in df_libros['titulo'].str.lower().values:
        idx = df_libros[df_libros['titulo'].str.lower() == titulo].index[0]

        if df_libros.at[idx, 'estado'] == 'disponible':
            df_libros.at[idx, 'estado'] = 'vendido'
            df_libros.at[idx, 'fecha_venta'] = dt.datetime.now().strftime("%Y-%m-%d")
            print(f"Libro '{df_libros.at[idx, 'titulo']}' vendido por {df_libros.at[idx, 'precio']} el {df_libros.at[idx, 'fecha_venta']}")
        else:
            print("Libro no disponible para la venta")
    else:
        print("Libro no encontrado")
    menu()

def prestar_libro():
    titulo = input("Ingrese el título del libro a prestar: ").strip().lower()
    if titulo in df_libros['titulo'].str.lower().values:
        idx = df_libros[df_libros['titulo'].str.lower() == titulo].index[0]

        if df_libros.at[idx, 'estado'] == 'disponible':
            df_libros.at[idx, 'estado'] = 'prestado'
            df_libros.at[idx, 'prestado_a'] = input("Ingrese el nombre de la persona a quien se le presta: ")
            fecha_actual = dt.datetime.now()
            fecha_devolucion = fecha_actual + dt.timedelta(days=7)
            df_libros.at[idx, 'fecha_devolucion'] = fecha_devolucion.strftime("%Y-%m-%d")
            print(f"Libro '{df_libros.at[idx, 'titulo']}' prestado a {df_libros.at[idx, 'prestado_a']} hasta el {df_libros.at[idx, 'fecha_devolucion']}")
        else:
            print("Libro no disponible para el préstamo")
    else:
        print("Libro no encontrado")
    menu()

def buscar_libro():
    titulo = input("Ingrese el título del libro a buscar: ").strip().lower()
    if titulo in df_libros['titulo'].str.lower().values:
        idx = df_libros[df_libros['titulo'].str.lower() == titulo].index[0]

        if df_libros.at[idx, 'estado'] == 'vendido':
            print(f"Libro: '{df_libros.at[idx, 'titulo']}'\nAutor: '{df_libros.at[idx, 'autor']}'\nFue vendido por: {df_libros.at[idx, 'precio']} el {df_libros.at[idx, 'fecha_venta']}")

        elif df_libros.at[idx, 'estado'] == 'prestado':
            print(f"Libro: '{df_libros.at[idx, 'titulo']}'\nAutor: '{df_libros.at[idx, 'autor']}'\nPrestado a: {df_libros.at[idx, 'prestado_a']}\nFecha de devolución: {df_libros.at[idx, 'fecha_devolucion']}")
            print(f"Fecha actual: {dt.datetime.now().strftime('%Y-%m-%d')}")
            fecha_devolucion = dt.datetime.strptime(df_libros.at[idx, 'fecha_devolucion'], "%Y-%m-%d")

            if fecha_devolucion < dt.datetime.now():
                dias_retraso = (dt.datetime.now() - fecha_devolucion).days
                print(f"Fecha de devolución vencida. Días de retraso: {dias_retraso}")
            else:
                print(f"Días restantes para la devolución: {fecha_devolucion - dt.datetime.now()}")
        else:
            print(f"Libro '{df_libros.at[idx, 'titulo']}' está disponible")
            print(f"Autor: {df_libros.at[idx, 'autor']}\nGénero: {df_libros.at[idx, 'genero']}\nFecha de emisión: {df_libros.at[idx, 'fecha_emision']}\nPrecio: {df_libros.at[idx, 'precio']}")
    else:
        print("Libro no encontrado")
    menu()

inicio()