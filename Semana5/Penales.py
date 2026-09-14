# Importamos la biblioteca para generar valores aleatorios.
import random

# Mostramos el nombre del juego.
print("=== TORNEO DE PENALES ===")

# Solicitamos el nombre del jugador.
nombre_jugador = input("Escribe tu nombre: ")

# Creamos una lista con las direcciones disponibles.
direcciones = ["izquierda", "centro", "derecha"]

# Contadores de goles.
goles_jugador = 0
goles_computadora = 0

# Listas para guardar los resultados de las rondas.
resultados_jugador = []
resultados_computadora = []

# Se jugarán cinco rondas.
for ronda in range(1, 6):

    print()
    print("==============================")
    print("RONDA", ronda)
    print("==============================")

    # Mostramos el marcador.
    print(
        "Marcador:",
        nombre_jugador,
        goles_jugador,
        "-",
        goles_computadora,
        "Computadora"
    )

    # ----------------------------------------
    # TURNO DEL JUGADOR
    # ----------------------------------------

    print()
    print("Es tu turno de disparar.")
    print("1. Izquierda")
    print("2. Centro")
    print("3. Derecha")

    # Solicitamos la dirección del disparo.
    direccion_jugador = int(
        input("Elige la dirección del disparo: ")
    )

    # Validamos que la opción esté entre 1 y 3.
    while direccion_jugador < 1 or direccion_jugador > 3:

        print("Opción incorrecta. Elige 1, 2 o 3.")

        direccion_jugador = int(
            input("Elige nuevamente la dirección: ")
        )

    # La computadora elige hacia dónde lanzarse.
    direccion_portero = random.randint(1, 3)

    # Mostramos las direcciones seleccionadas.
    print(
        "==============================\n"
        "Disparaste hacia:",
        direcciones[direccion_jugador - 1]
    )

    print(
        "==============================\n"
        "El portero se lanzó hacia:",
        direcciones[direccion_portero - 1]
    )

    with open("intentos_penales.txt", "a") as archivo:
        archivo.write(f"Intento del jugador: {direcciones[direccion_jugador - 1]} - Fallado\n")

    # Si las direcciones coinciden, el portero detiene el balón.
    if direccion_jugador == direccion_portero:

        print(
            "---------------------------------\n"
              "¡El portero detuvo el penal!")

        # Guardamos el resultado.
        resultados_jugador.append("fallado")

    # Si son diferentes, el jugador anota.
    else:

        print("----¡Gooooool de", nombre_jugador,"!----")

        # Aumentamos el marcador.
        goles_jugador = goles_jugador + 1

        # Guardamos el resultado.
        resultados_jugador.append("gol")

    # ----------------------------------------
    # TURNO DE LA COMPUTADORA
    # ----------------------------------------

    print()
    print("Ahora la computadora realizará su disparo.")
    print("Tú eres el portero.")
    print("1. Lanzarte a la izquierda")
    print("2. Permanecer en el centro")
    print("3. Lanzarte a la derecha")

    # Solicitamos la decisión del jugador.
    direccion_defensa = int(
        input("Elige hacia dónde lanzarte: ")
    )

    # Validamos que la dirección sea correcta.
    while direccion_defensa < 1 or direccion_defensa > 3:

        print("Opción incorrecta. Elige 1, 2 o 3.")

        direccion_defensa = int(
            input("Elige nuevamente la dirección: ")
        )

    # La computadora elige aleatoriamente su disparo.
    direccion_computadora = random.randint(1, 3)

    # Mostramos las decisiones.
    print(
        "==============================\n"
        "Te lanzaste hacia:",
        direcciones[direccion_defensa - 1]
    )

    print(
        "==============================\n"
        "La computadora disparó hacia:",
        direcciones[direccion_computadora - 1]
    )

    # Si coinciden, el jugador detiene el penal.
    if direccion_defensa == direccion_computadora:

        print(
            "---------------------------------\n"
              "¡Atajaste el penal!")

        # Guardamos el resultado.
        resultados_computadora.append("fallado")
        #Intentos de la computadora
        with open("intentos_penales.txt", "a") as archivo:
            archivo.write(f"Intento de la computadora: {direcciones[direccion_computadora - 1]} - Fallado\n")

    # Si las direcciones son diferentes, la computadora anota.
    else:

        print("La computadora anotó un gol.")

        # Aumentamos sus goles.
        goles_computadora = goles_computadora + 1

        # Guardamos el resultado.
        resultados_computadora.append("gol")


# Mostramos el marcador final.
print()
print("=== MARCADOR FINAL ===")

print(
    nombre_jugador,
    goles_jugador,
    "-",
    goles_computadora,
    "Computadora"
)

# Determinamos al ganador.
if goles_jugador > goles_computadora:

    print("¡Felicidades,", nombre_jugador, "!")
    print("Ganaste el torneo de penales.")

elif goles_computadora > goles_jugador:

    print("La computadora ganó el torneo.")
    print("Solicitamos revisión del VAR... quizá era un bug.")

else:

    print("El torneo terminó empatado.")


# Mostramos el historial del jugador.
print()
print("Resultados de", nombre_jugador, ":")

for resultado in resultados_jugador:
    print(resultado, end=" ")

# Mostramos el historial de la computadora.
print()
print("Resultados de la computadora:")

for resultado in resultados_computadora:
    print(resultado, end=" ")

print()
print("=== FIN DEL JUEGO ===")