def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

def verificar_ganador(tablero, jugador):
    # Verificar filas, columnas y diagonales
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def tablero_lleno(tablero):
    return all(tablero[i][j] != " " for i in range(3) for j in range(3))

def tres_en_raya():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)
        print(f"Turno del jugador {jugador_actual}")
        fila = int(input("Ingresa la fila (0, 1, 2): "))
        columna = int(input("Ingresa la columna (0, 1, 2): "))

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual
            if verificar_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"¡El jugador {jugador_actual} ha ganado!")
                break
            elif tablero_lleno(tablero):
                imprimir_tablero(tablero)
                print("¡Es un empate!")
                break
            jugador_actual = "O" if jugador_actual == "X" else "X"
        else:
            print("La posición ya está ocupada. Intenta de nuevo.")

if __name__ == "__main__":
    tres_en_raya()