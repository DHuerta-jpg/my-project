import random

FILAS = 5
COLUMNAS = 5

def crear_oceano():
    # Lista de listas: una lista con 5 filas, cada fila con 5 columnas
    return [["agua" for _ in range(COLUMNAS)] for _ in range(FILAS)]

def mostrar_oceano(oceano, revelar=False):
    print("   " + "  ".join(str(c + 1) for c in range(COLUMNAS)))
    for i, fila in enumerate(oceano):
        fila_mostrar = []
        for celda in fila:
            if celda == "Barco" and not revelar:
                fila_mostrar.append("~")  # oculta el barco
            elif celda == "agua":
                fila_mostrar.append("~")
            else:
                fila_mostrar.append(celda[0])  # "B" o "X"
        print(f"{i + 1}  " + "  ".join(fila_mostrar))
    print()

def jugar():
    oceano = crear_oceano()

    fila_barco = random.randint(0, FILAS - 1)
    col_barco = random.randint(0, COLUMNAS - 1)
    oceano[fila_barco][col_barco] = "Barco"

    intentos = 5
    barco_encontrado = False

    while intentos > 0:
        mostrar_oceano(oceano)
        try:
            fila = int(input(f"Elige una fila (1-{FILAS}): ")) - 1
            col = int(input(f"Elige una columna (1-{COLUMNAS}): ")) - 1
        except ValueError:
            print("Debes ingresar números.")
            continue

        if not (0 <= fila < FILAS and 0 <= col < COLUMNAS):
            print(f"La fila y columna deben estar entre 1 y {FILAS}.")
            continue

        if oceano[fila][col] == "Barco":
            oceano[fila][col] = "X"
            print("¡Impacto! Hundiste el barco.")
            barco_encontrado = True
            break
        else:
            oceano[fila][col] = "X"  # marca el disparo fallido
            print("¡Agua!")
            intentos -= 1
            print("Intentos disponibles:", intentos)

    mostrar_oceano(oceano, revelar=True)

    if barco_encontrado:
        print("¡Ganaste la batalla naval!")
    else:
        print("El barco escapó.")
        print(f"Estaba en la fila {fila_barco + 1}, columna {col_barco + 1}")

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