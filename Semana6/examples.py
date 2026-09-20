import random

DIMENSION = 3


# Imprime el tablero con el formato gráfico ASCII
def mostrar_tablero(tablero):
    print("+-------+-------+-------+")
    for fila in range(DIMENSION):
        print("|       |       |       |")
        print(
            f"|   {tablero[fila][0]}   |   {tablero[fila][1]}   |   {tablero[fila][2]}   |"
        )
        print("|       |       |       |")
        print("+-------+-------+-------+")


# Revisa si un símbolo ('X' u 'O') ha ganado
def verificar_ganador(tablero, jugador):
    for i in range(DIMENSION):
        # Filas y columnas
        if all(tablero[i][j] == jugador for j in range(DIMENSION)):
            return True
        if all(tablero[j][i] == jugador for j in range(DIMENSION)):
            return True

    # Diagonales
    if all(tablero[i][i] == jugador for i in range(DIMENSION)):
        return True
    if all(tablero[i][DIMENSION - 1 - i] == jugador for i in range(DIMENSION)):
        return True

    return False


# Obtiene la lista de números que siguen disponibles en el tablero
def casillas_libres(tablero):
    libres = []
    for fila in range(DIMENSION):
        for col in range(DIMENSION):
            if tablero[fila][col] not in ["X", "O"]:
                libres.append((fila, col))
    return libres


def jugar():
    # Inicialización: números del '1' al '9'
    tablero = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]

    # La máquina inicia al centro ('5' -> fila 1, col 1)
    tablero[1][1] = "X"

    while True:
        mostrar_tablero(tablero)

        libres = casillas_libres(tablero)
        if not libres:
            print("¡Empate!")
            break

        # --- TURNO JUGADOR ('O') ---
        try:
            movimiento = int(input("Ingresa tu movimiento: "))
        except ValueError:
            print("Por favor ingresa un número válido (1-9).\n")
            continue

        if movimiento < 1 or movimiento > 9:
            print("Movimiento fuera de rango. Elige entre 1 y 9.\n")
            continue

        # Convertir número 1-9 a coordenada (fila, col)
        fila = (movimiento - 1) // 3
        col = (movimiento - 1) % 3

        if tablero[fila][col] in ["X", "O"]:
            print("Esa casilla ya está ocupada. Elige otra.\n")
            continue

        tablero[fila][col] = "O"

        if verificar_ganador(tablero, "O"):
            mostrar_tablero(tablero)
            print("¡Has Ganado!")
            break

        libres = casillas_libres(tablero)
        if not libres:
            mostrar_tablero(tablero)
            print("¡Empate!")
            break

        # --- TURNO MÁQUINA ('X') ---
        fila_ia, col_ia = random.choice(libres)
        tablero[fila_ia][col_ia] = "X"

        if verificar_ganador(tablero, "X"):
            mostrar_tablero(tablero)
            print("¡La máquina ha ganado!")
            break


def main():
    jugar()


main()