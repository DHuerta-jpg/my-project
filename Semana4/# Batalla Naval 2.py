# Batalla Naval 2.0

import random

DIMENSION = 5
NUM_BARCOS = 5

# muestra el tablero real (con los barcos visibles)
def mostrar_tablero_real(tablero):
    for fila in range(DIMENSION):
        for columna in range(DIMENSION):
            print(tablero[fila][columna], end=" ")
        print()

# muestra el tablero visible (lo que ve el jugador)
def mostrar_tablero(tablero_visible):
    for fila in range(DIMENSION):
        print(f"{fila + 1}: ", end=" ")
        for columna in range(DIMENSION):
            print(tablero_visible[fila][columna], end=" ")
        print()

# Juego
def jugar():
    # tablero inicia vacío
    tablero = []
    tablero_visible = []

    # se crea el tablero con agua
    for fila in range(DIMENSION):
        nueva_fila = []
        nueva_fila_visible = []
        for columna in range(DIMENSION):
            nueva_fila.append("agua")
            nueva_fila_visible.append("~")
        tablero.append(nueva_fila)
        tablero_visible.append(nueva_fila_visible)

    # Colocar barcos de manera aleatoria en el tablero
    barcos = 0
    while barcos < NUM_BARCOS:
        fila = random.randint(0, DIMENSION - 1)
        columna = random.randint(0, DIMENSION - 1)
        if tablero[fila][columna] == "agua":
            tablero[fila][columna] = "barco"
            barcos += 1

    intentos = 8
    barco_encontrado = False

    # Mientras tengas intentos y no hayas hundido todos los barcos
    while intentos > 0:
        mostrar_tablero(tablero_visible)
        print("Intentos disponibles:", intentos)

        fila_x = int(input("Elige una fila: "))
        columna_y = int(input("Elige una columna: "))

        if fila_x >= 1 and fila_x <= DIMENSION and columna_y >= 1 and columna_y <= DIMENSION:
            fila_matriz = fila_x - 1
            columna_matriz = columna_y - 1

            if tablero[fila_matriz][columna_matriz] == "barco":
                print("¡Impacto! Acertaste.")
                tablero_visible[fila_matriz][columna_matriz] = "X"
                barcos -= 1
                if barcos == 0:
                    barco_encontrado = True
                    break
            else:
                print("¡Agua!")
                tablero_visible[fila_matriz][columna_matriz] = "O"
                intentos -= 1
                print()
        else:
            print("Debe estar en el rango válido")
            continue

    mostrar_tablero_real(tablero)

    if barco_encontrado == False:
        print("Se te acabaron los intentos. Perdiste.")
    else:
        print("¡Hundiste todos los barcos! Ganaste la batalla naval!")


def main():
    print("=== BATALLA NAVAL ===")
    while True:
        jugar()
        opcion = input("¿Deseas jugar otra vez? (s/n): ").lower()
        if opcion != "s":
            print("================================")
            print("Gracias por jugar. ¡Hasta luego!")
            break

main()