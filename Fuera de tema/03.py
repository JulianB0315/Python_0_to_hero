import random
import time

# Constantes
TRACK_LENGTH = 50

def print_track(car1_pos, car2_pos):
    track1 = "-" * car1_pos + "🛸" + "-" * (TRACK_LENGTH - car1_pos)
    track2 = "-" * car2_pos + "🛩️" + "-" * (TRACK_LENGTH - car2_pos)
    print(f"Carro 1: {track1}")
    print(f"Carro 2: {track2}")

def race():
    car1_pos = 0
    car2_pos = 0

    while car1_pos < TRACK_LENGTH and car2_pos < TRACK_LENGTH:
        car1_pos += random.randint(1, 3)
        car2_pos += random.randint(1, 3)
        
        # Limita la posición a la longitud de la pista
        car1_pos = min(car1_pos, TRACK_LENGTH)
        car2_pos = min(car2_pos, TRACK_LENGTH)
        
        print_track(car1_pos, car2_pos)
        time.sleep(0.5)
        print("\n" * 20)  # Limpiar la pantalla

    if car1_pos >= TRACK_LENGTH and car2_pos >= TRACK_LENGTH:
        print("¡Es un empate!")
    elif car1_pos >= TRACK_LENGTH:
        print("¡El platillo volador gana!")
    else:
        print("¡El Avion gana!")

if __name__ == "__main__":
    race()
