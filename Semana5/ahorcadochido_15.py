# Ahorcado
import random

# Lista de dibujos durante el juego
dibujos = [
    [
        "  _______",
        "  |     |",
        "  |",
        "  |",
        "  |",
        "  |",
        "=========\n",
    ],
    [
        "  _______",
        "  |     |",
        "  |     ☺︎",
        "  |",
        "  |",
        "  |",
        "=========\n",
    ],
    [
        "  _______",
        "  |     |",
        "  |     ☺︎",
        "  |     |",
        "  |",
        "  |",
        "=========\n",
    ],
    [
        "  _______",
        "  |     |",
        "  |     ☺︎",
        "  |    /|",
        "  |",
        "  |",
        "=========\n",
    ],
    [
        "  _______",
        "  |     |",
        "  |     ㋡",
        "  |    /|\\",
        "  |",
        "  |",
        "=========\n",
    ],
    [
        "  _______",
        "  |     |",
        "  |     ☹",
        "  |    /|\\",
        "  |    /",
        "  |",
        "=========\n",
    ],
    [
        "  _______",
        "  |     |",
        "  |     ☹",
        "  |    /|\\",
        "  |    / \\",
        "  |",
        "=========\n",
    ],
]

# Dibujo especial para cuando se GANA la partida (liberado de la horca)
dibujo_victoria = [
    "  _______        ",
    "  |     |       \\☺︎/",
    "  |              | ",
    "  |             / \\",
    "  |          ¡LIBRE!",
    "  |              ",
    "=========\n",
]


# Mostrar dibujo según número de errores
def mostrar_dibujo(errores):
    dibujo_actual = dibujos[errores]
    for linea in dibujo_actual:
        print(linea)


# Mostrar dibujo victorioso
def mostrar_victoria():
    for linea in dibujo_victoria:
        print(linea)


# Guardar intentos en archivo
def guardar_partida(palabra_secreta, resultado, intento):
    with open("historial_intentos.txt", "a") as archivo:
        archivo.write("=================================\n")
        archivo.write(f"Palabra secreta: {palabra_secreta}\n")
        archivo.write(f"Resultado: {resultado}\n")
        archivo.write(f"Intentos realizados: {','.join(intento)}\n")
        archivo.write("=================================\n")


# Partida Completa
def jugar():
    palabra_secreta = random.choice([
        "salsa",
        "frijoles",
        "nopal",
        "mezcal",
        "esquites",
        "mole",
        "elotes",
        "chilaquiles",
        "maiz",
        "tortilla",
        "enfrijoladas",
        "tostadas",
        "memelas",
        "taco",
        "tamal",
        "pozole",
        "tequila",
        "pulque",
        "tepache",
        "atole",
        "tejate",
        "pozol",
    ])
    palabra_visible = ["_"] * len(palabra_secreta)
    letras_adivinadas = []
    vidas = 6
    errores = 0

    while True:
        print()

        # Comprobación de Victoria
        if "".join(palabra_visible) == palabra_secreta:
            mostrar_victoria()
            print("Palabra:", " ".join(palabra_visible))
            print(
                "\n¡Felicidades! Has salvado al monito. La palabra era:",
                palabra_secreta.upper(),
            )
            guardar_partida(palabra_secreta, "Victoria", letras_adivinadas)
            break

        # Comprobación de Derrota
        if vidas == 0:
            mostrar_dibujo(errores)
            print("Palabra:", " ".join(palabra_visible))
            print("\n¡Has perdido! La palabra era:", palabra_secreta.upper())
            guardar_partida(palabra_secreta, "Derrota", letras_adivinadas)
            break

        mostrar_dibujo(errores)
        print("Palabra:", " ".join(palabra_visible))
        print("Letras utilizadas:", " ".join(letras_adivinadas))
        print(f"Vidas restantes: {vidas}")
        print(f"Errores: {errores}")

        # Pedir letra al usuario
        intento = input("\nIngresa una letra: ").lower()

        # Validaciones de entrada
        if not intento or len(intento) > 1:
            print("Por favor, ingresa solo una letra.")
            continue

        if intento in letras_adivinadas:
            print("Ya habías ingresado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(intento)

        # Actualizar estado
        if intento in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if intento == palabra_secreta[i]:
                    palabra_visible[i] = intento
        else:
            errores += 1
            vidas -= 1
            print(f"Letra incorrecta. Te quedan {vidas} vidas.")


# Menú principal
def main():
    print("==========================================")
    print("\t--------Ahorcado--------")
    print("\t ---Comida Mexicana---")
    while True:
        jugar()
        opcion = input("\n¿Deseas jugar otra vez? (s/n): ").lower()
        if opcion != "s":
            print("================================")
            print("Gracias por jugar. ¡Hasta luego!")
            break


main()