import time
import os
import random

Libros = [
    {"titulo": "El Resplandor", "autor": "Stephen King", "genero": "Terror", "fecha_emision": "1977", "estado": "disponible", "precio": 25.0},
    {"titulo": "Drácula", "autor": "Bram Stoker", "genero": "Terror", "fecha_emision": "1897", "estado": "vendido", "precio": 18.0, "fecha_venta": "2023-01-15"},
    {"titulo": "El Padrino", "autor": "Mario Puzo", "genero": "Acción", "fecha_emision": "1969", "estado": "disponible", "precio": 22.0},
    {"titulo": "Matar a un ruiseñor", "autor": "Harper Lee", "genero": "Drama", "fecha_emision": "1960", "estado": "prestado", "precio": 15.0, "prestado_a": "Juan Perez", "fecha_devolucion": "2023-12-01"},
    {"titulo": "La lista de Schindler", "autor": "Thomas Keneally", "genero": "Drama", "fecha_emision": "1982", "estado": "disponible", "precio": 20.0},
    {"titulo": "Cementerio de animales", "autor": "Stephen King", "genero": "Terror", "fecha_emision": "1983", "estado": "disponible", "precio": 24.0},
    {"titulo": "El silencio de los inocentes", "autor": "Thomas Harris", "genero": "Terror", "fecha_emision": "1988", "estado": "disponible", "precio": 19.0},
    {"titulo": "Misión imposible", "autor": "Bruce Geller", "genero": "Acción", "fecha_emision": "1966", "estado": "prestado", "precio": 21.0, "prestado_a": "Maria Lopez", "fecha_devolucion": "2023-11-20"},
    {"titulo": "Gladiador", "autor": "Dewey Gram", "genero": "Acción", "fecha_emision": "2000", "estado": "disponible", "precio": 23.0},
    {"titulo": "El gran Gatsby", "autor": "F. Scott Fitzgerald", "genero": "Drama", "fecha_emision": "1925", "estado": "vendido", "precio": 17.0, "fecha_venta": "2023-02-10"}
]

class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
    def __str__(self):
        return f"{self.titulo} de {self.autor}"

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
    print("Menú de la biblioteca")
    print("1. Ver libros")
    print("2. Vender libro")
    print("3. Prestar libro")
    print("4. Buscar libro")
    print("5. Salir")
    opcion = input()
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
    elif opcion == "6":
        carrera_de_buses()
    else:
        print("Opción inválida")
        menu()

def ver_libros():
    for libro in Libros:
        print(f"{libro['titulo']} de {libro['autor']} - {libro['genero']} ({libro['fecha_emision']}) - {libro['estado']}")
    menu()

def vender_libro():
    titulo = input("Ingrese el título del libro a vender: ")
    for libro in Libros:
        if libro["titulo"].lower() == titulo.lower() and libro["estado"] == "disponible":
            libro["estado"] = "vendido"
            libro["fecha_venta"] = input("Ingrese la fecha de venta: ")
            print(f"Libro '{libro['titulo']}' vendido por {libro['precio']} el {libro['fecha_venta']}")
            break
    else:
        print("Libro no encontrado o no disponible")
    menu()

def prestar_libro():
    titulo = input("Ingrese el título del libro a prestar: ")
    for libro in Libros:
        if libro["titulo"].lower() == titulo.lower() and libro["estado"] == "disponible":
            libro["estado"] = "prestado"
            libro["prestado_a"] = input("Ingrese el nombre de la persona a quien se le presta: ")
            libro["fecha_devolucion"] = input("Ingrese la fecha de devolución: ")
            print(f"Libro '{libro['titulo']}' prestado a {libro['prestado_a']} hasta el {libro['fecha_devolucion']}")
            break
    else:
        print("Libro no encontrado o no disponible")
    menu()

def buscar_libro():
    titulo = input("Ingrese el título del libro a buscar: ").strip().lower()
    for libro in Libros:
        if libro["titulo"].strip().lower() == titulo:
            if libro["estado"] == "vendido":
                print(f"Libro '{libro['titulo']}' fue vendido por {libro['precio']} el {libro['fecha_venta']}")
            elif libro["estado"] == "prestado":
                print(f"Libro '{libro['titulo']}' fue prestado a {libro['prestado_a']} hasta el {libro['fecha_devolucion']}")
            else:
                print(f"Libro '{libro['titulo']}' está disponible")
            break
    else:
        print("Libro no encontrado")
    menu()
def carrera_de_buses():
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    print("Carrera de buses")
    buses = [
        {"nombre": "El Chino      🏁", "velocidad": random.randint(1, 100), "distancia": 0},
        {"nombre": "El loro       🏁", "velocidad": random.randint(1, 100), "distancia": 0},
        {"nombre": "Todo Vise     🏁", "velocidad": random.randint(1, 100), "distancia": 0},
        {"nombre": "Modelo        🏁", "velocidad": random.randint(1, 100), "distancia": 0},
        {"nombre": "Mototaxi toro 🏁", "velocidad": random.randint(1, 100), "distancia": 0}
    ]
    distancia_meta = 1000
    ganador = None

    while not ganador:
        clear_screen()
        for bus in buses:
            bus["velocidad"] = random.randint(1, 100)  # Cambiar la velocidad en cada iteración
            bus["distancia"] += bus["velocidad"]
            if bus["distancia"] >= distancia_meta:
                ganador = bus["nombre"]
        
        for bus in buses:
            barra = "#" * (bus["distancia"] * 50 // distancia_meta)
            print(f"{bus['nombre']}: {barra} {bus['distancia']}m")
        
        time.sleep(1)

    print(f"\n{ganador} ha ganado la carrera")

inicio()