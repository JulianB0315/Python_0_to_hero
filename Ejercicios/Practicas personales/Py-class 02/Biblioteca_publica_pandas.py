import pandas as pd
import datetime as dt

Libros = [
    {"titulo": "El Resplandor", "autor": "Stephen King", "genero": "Terror", "fecha_emision": "1977", "estado": "disponible", "precio": 25.0},
    {"titulo": "Drácula", "autor": "Bram Stoker", "genero": "Terror", "fecha_emision": "1897", "estado": "vendido", "precio": 18.0, "fecha_venta": "2023-01-15"},
    {"titulo": "El Padrino", "autor": "Mario Puzo", "genero": "Acción", "fecha_emision": "1969", "estado": "disponible", "precio": 22.0},
    {"titulo": "Matar a un ruiseñor", "autor": "Harper Lee", "genero": "Drama", "fecha_emision": "1960", "estado": "prestado", "precio": 15.0, "prestado_a": "Juan Perez", "fecha_devolucion": "2023-12-01"},
    {"titulo": "La lista de Schindler", "autor": "Thomas Keneally", "genero": "Drama", "fecha_emision": "1982", "estado": "disponible", "precio": 20.0},
    {"titulo": "Cementerio de animales", "autor": "Stephen King", "genero": "Terror", "fecha_emision": "1983", "estado": "disponible", "precio": 24.0},
    {"titulo": "El silencio de los inocentes", "autor": "Thomas Harris", "genero": "Terror", "fecha_emision": "1988", "estado": "disponible", "precio": 19.0},
    {"titulo": "Misión imposible", "autor": "Bruce Geller", "genero": "Acción", "fecha_emision": "1966", "estado": "prestado", "precio": 21.0, "prestado_a": "Maria Lopez", "fecha_devolucion": "2025-11-20"},
    {"titulo": "Gladiador", "autor": "Dewey Gram", "genero": "Acción", "fecha_emision": "2000", "estado": "disponible", "precio": 23.0},
    {"titulo": "El gran Gatsby", "autor": "F. Scott Fitzgerald", "genero": "Drama", "fecha_emision": "1925", "estado": "vendido", "precio": 17.0, "fecha_venta": "2023-02-10"},
    {"titulo": "Carrie", "autor": "Stephen King", "genero": "Terror", "fecha_emision": "1974", "estado": "disponible", "precio": 20.0},
    {"titulo": "It", "autor": "Stephen King", "genero": "Terror", "fecha_emision": "1986", "estado": "vendido", "precio": 25.0, "fecha_venta": "2023-03-01"},
    {"titulo": "El hombre invisible", "autor": "H.G. Wells", "genero": "Terror", "fecha_emision": "1897", "estado": "disponible", "precio": 18.0},
    {"titulo": "Psicosis", "autor": "Robert Bloch", "genero": "Terror", "fecha_emision": "1959", "estado": "vendido", "precio": 22.0, "fecha_venta": "2023-04-10"},
    {"titulo": "El exorcista", "autor": "William Peter Blatty", "genero": "Terror", "fecha_emision": "1971", "estado": "disponible", "precio": 24.0},
    {"titulo": "El fugitivo", "autor": "Stephen King", "genero": "Acción", "fecha_emision": "1982", "estado": "disponible", "precio": 21.0},
    {"titulo": "El último mohicano", "autor": "James Fenimore Cooper", "genero": "Acción", "fecha_emision": "1826", "estado": "vendido", "precio": 19.0, "fecha_venta": "2023-05-15"},
    {"titulo": "Rambo", "autor": "David Morrell", "genero": "Acción", "fecha_emision": "1972", "estado": "disponible", "precio": 23.0},
    {"titulo": "La jungla de cristal", "autor": "Roderick Thorp", "genero": "Acción", "fecha_emision": "1979", "estado": "vendido", "precio": 20.0, "fecha_venta": "2023-06-20"},
    {"titulo": "El código Da Vinci", "autor": "Dan Brown", "genero": "Acción", "fecha_emision": "2003", "estado": "disponible", "precio": 22.0},
    {"titulo": "Los miserables", "autor": "Victor Hugo", "genero": "Drama", "fecha_emision": "1862", "estado": "disponible", "precio": 25.0},
    {"titulo": "Orgullo y prejuicio", "autor": "Jane Austen", "genero": "Drama", "fecha_emision": "1813", "estado": "vendido", "precio": 18.0, "fecha_venta": "2023-07-25"},
    {"titulo": "Cumbres borrascosas", "autor": "Emily Brontë", "genero": "Drama", "fecha_emision": "1847", "estado": "disponible", "precio": 20.0},
    {"titulo": "Rebelión en la granja", "autor": "George Orwell", "genero": "Drama", "fecha_emision": "1945", "estado": "vendido", "precio": 15.0, "fecha_venta": "2023-08-30"},
    {"titulo": "1984", "autor": "George Orwell", "genero": "Drama", "fecha_emision": "1949", "estado": "disponible", "precio": 22.0},
    {"titulo": "El guardián entre el centeno", "autor": "J.D. Salinger", "genero": "Drama", "fecha_emision": "1951", "estado": "vendido", "precio": 19.0, "fecha_venta": "2023-09-05"},
    {"titulo": "El gran escape", "autor": "Paul Brickhill", "genero": "Acción", "fecha_emision": "1950", "estado": "disponible", "precio": 21.0},
    {"titulo": "El hombre de acero", "autor": "Larry Tye", "genero": "Acción", "fecha_emision": "2012", "estado": "vendido", "precio": 24.0, "fecha_venta": "2023-10-10"},
    {"titulo": "El club de la pelea", "autor": "Chuck Palahniuk", "genero": "Acción", "fecha_emision": "1996", "estado": "disponible", "precio": 23.0},
    {"titulo": "El señor de los anillos", "autor": "J.R.R. Tolkien", "genero": "Acción", "fecha_emision": "1954", "estado": "vendido", "precio": 25.0, "fecha_venta": "2023-11-15"},
    {"titulo": "El hobbit", "autor": "J.R.R. Tolkien", "genero": "Acción", "fecha_emision": "1937", "estado": "disponible", "precio": 20.0}
]

df_libros = pd.DataFrame(Libros)

def iniciar_sesion():
    print("Iniciar sesión")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    if usuario == "admin" and contrasena == "admin":
        print("Sesión iniciada")
        menu()
    else:
        print("Usuario no encontrado")
        inicio()

def inicio():
    print("Bienvenido a la biblioteca pública")
    print("1. Iniciar sesión")
    print("2. Salir")
    opcion = input()
    if opcion == "1":
        iniciar_sesion()
    elif opcion == "2":
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
    print("5. Salir")
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
        print("Gracias por usar la biblioteca")
        if input("¿Desea guardar los cambios? (si/no): ").strip().lower() == "si":
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
            df_libros.at[idx, 'fecha_venta'] = input("Ingrese la fecha de venta: ")
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