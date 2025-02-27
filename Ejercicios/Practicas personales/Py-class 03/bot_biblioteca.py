import re 
import random
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import Biblioteca_publica_IA as biblioteca

df_libros = pd.read_csv('Ejercicios/Practicas personales/Py-class 03/libros.csv')

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
        return negativa_response()
    return positive_response()

def vender_libro():
    titulo = input("Ingrese el título del libro a vender: ").strip().lower()

    if titulo in df_libros['titulo'].str.lower().values:
        idx = df_libros[df_libros['titulo'].str.lower() == titulo].index[0]

        if df_libros.at[idx, 'estado'] == 'disponible':
            df_libros.at[idx, 'estado'] = 'vendido'
            df_libros.at[idx, 'fecha_venta'] = dt.datetime.now().strftime("%Y-%m-%d")
            df_libros.at[idx, 'prestado_a'] = ''
            df_libros.at[idx, 'fecha_devolucion'] = ''
            print(f"Libro '{df_libros.at[idx, 'titulo']}' vendido por {df_libros.at[idx, 'precio']} el {df_libros.at[idx, 'fecha_venta']}")
            df_libros.to_csv('Ejercicios/Practicas personales/Py-class 03/libros.csv', index=False)
            return positive_response()
        else:
            print("Libro no disponible para la venta")
    else:
        print("Libro no encontrado")
    return negativa_response()

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
            df_libros.at[idx, 'fecha_venta'] = ''
            print(f"Libro '{df_libros.at[idx, 'titulo']}' prestado a {df_libros.at[idx, 'prestado_a']} hasta el {df_libros.at[idx, 'fecha_devolucion']}")
            df_libros.to_csv('Ejercicios/Practicas personales/Py-class 03/libros.csv', index=False)
            return positive_response()
        else:
            print("Libro no disponible para el préstamo")
    else:
        print("Libro no encontrado")
        return negativa_response()

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
                return positive_response()
            else:
                print(f"Días restantes para la devolución: {fecha_devolucion - dt.datetime.now()}")
                return positive_response()
            
        else:
            print(f"Libro '{df_libros.at[idx, 'titulo']}' está disponible")
            print(f"Autor: {df_libros.at[idx, 'autor']}\nGénero: {df_libros.at[idx, 'genero']}\nFecha de emisión: {df_libros.at[idx, 'fecha_emision']}\nPrecio: {df_libros.at[idx, 'precio']}")
            return positive_response()
    else:
        print("Libro no encontrado")
        return negativa_response()

def get_response(user_input):
    split_message = re.split(r'\s|,|;|:', user_input.lower())
    response = check_for_greeting(split_message)
    return response

def mesage_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_for_greeting(message):
    high_prob={}

    def reponse(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal high_prob
        high_prob[bot_response] = mesage_probability(message, list_of_words, single_response, required_words)

    reponse('Hola, causa. ¿Qué tal la vida?', ['hola', 'saludos', 'buenas', 'que tal', 'oe causa', 'manito'], single_response=True)
    reponse('Estoy bien, mano, todo fresh. ¿Y tú?', ['como', 'estas', 'buenas', 'que tal', 'todo bien', 'como vas','bien y tu'], required_words=['como'])
    reponse('Estamos en Senati Chiclayo, firme. 📍', ['ubicados', 'direccion', 'donde', 'ubicacion', 'por donde queda', 'donde estan'], single_response=True)
    #Funciones de la biblioteca
    reponse('ver_libros', ['ver', 'libros'], required_words=['ver'])
    reponse('vender_libro', ['vender', 'libro', 'comprar', 'adquirir', 'vender libro', 'comprar libro'], required_words=['vender'])
    reponse('prestar_libro', ['prestar', 'libro','pedir'], required_words=['prestar'])
    reponse('buscar_libro', ['buscar', 'libro'], required_words=['buscar'])
    reponse('salir', ['salir', 'exit', 'terminar'], single_response=True)
    reponse('volver', ['menu', 'volver', 'regresar', 'inicio', 'principal'], single_response=True)

    best_match = max(high_prob, key=high_prob.get)
    if high_prob[best_match] < 1:
        return negativa_response()
    try:
        if best_match == "ver_libros":
            ver_libros()
            return positive_response()
        elif best_match == "vender_libro":
            vender_libro()
            return positive_response()
        elif best_match == "prestar_libro":
            prestar_libro()
            return positive_response()
        elif best_match == "buscar_libro":
            buscar_libro()
            return positive_response()
        elif best_match == "volver":
            print("Nos vidrios, causa. ¡Cuídate! 👋")
            biblioteca.menu()
        elif best_match == "salir":
            print("Nos vidrios, causa. ¡Cuídate! 👋")
            exit()
    except Exception:
        return negativa_response()

    return best_match

def positive_response():
    responses = [
        "¡Al toque, perro! Todo salió bien. 🐶",
        "¡Fierro! Ya quedó, ¿qué más necesitas? 🔥",
        "¡De la firme! Se hizo sin fallas. 💪",
        "¡Ya causa! Todo fresh, dime qué sigue. 😎",
        "¡Piña! Digo, ¡chévere! Se completó la acción. 🏆",
        "¡Habla, causita! ¿Algo más que quieras hacer? 🤙"
    ]
    return random.choice(responses)

def negativa_response():
    responses = [
        "Asuuu... creo que algo salió mal. 😵",
        "¡Qué palta! No se pudo completar. 🥑",
        "Uy no, esto está más tranca que examen de mate. 📚",
        "Piña, mano. No funcionó. 😬",
        "Tamos en la B, esto no jaló. 💀",
        "No hay forma, intenta de nuevo. 🤦‍♂️",
        "¡Ya fuiste, causa! Intenta otra vez. 🚫"
    ]
    return random.choice(responses)

def unknown():
    responses = [
        "No entiendo lo que dices.",
        "No sé qué quieres decir.",
        "¿Podrías repetirlo?",
        "Búscalo en algún navegador."
    ]
    return random.choice(responses)

if __name__ == '__main__':
    while True:
        print('Bot: ' + get_response(input('You: ')))