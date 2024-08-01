import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("¡Bienvenido al juego de Adivinar el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        guess = int(input("Ingresa tu suposición: "))
        attempts += 1

        if guess < number_to_guess:
            print("Demasiado bajo. Inténtalo de nuevo.")
        elif guess > number_to_guess:
            print("Demasiado alto. Inténtalo de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {attempts} intentos.")
            break

if __name__ == "__main__":
    guess_number()
