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

def inicializar_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]