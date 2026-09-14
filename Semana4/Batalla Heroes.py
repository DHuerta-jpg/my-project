# Importamos la biblioteca random.
import random

print("=== BATALLA DEL HÉROE ===")

# Vida inicial de los personajes.
vida_heroe = 50
vida_villano = 50

# Guardaremos aquí los ataques realizados por el héroe.
historial_ataques = []

# El juego continúa mientras ambos personajes tengan vida.
while vida_heroe > 0 and vida_villano > 0:

    print()
    print("Vida del héroe:", vida_heroe)
    print("Vida del villano:", vida_villano)

    print()
    print("1. Atacar")
    print("2. Curarse")

    opcion = int(input("Selecciona una opción: "))

    # Opción para atacar.
    if opcion == 1:

        # Generamos un ataque aleatorio entre 5 y 12.
        ataque_heroe = random.randint(5, 12)

        # Restamos el ataque a la vida del villano.
        vida_villano = vida_villano - ataque_heroe

        # Guardamos el ataque en la lista.
        historial_ataques.append(ataque_heroe)

 #HEROE       
        with open("historial_ataques.txt", "a") as archivo:
            archivo.write(f"Heroe: {ataque_heroe}\n")

        print("El héroe causó", ataque_heroe, "puntos de daño.")

    # Opción para recuperar vida.
    elif opcion == 2:

        # Generamos una cantidad aleatoria de curación.
        curacion = random.randint(4, 10)

        # Sumamos la curación a la vida del héroe.
        vida_heroe = vida_heroe + curacion

        # Evitamos que la vida supere el máximo permitido.
        if vida_heroe > 50:
            vida_heroe = 50

        print("El héroe recuperó", curacion, "puntos de vida.")

    # Se ejecuta si la opción no es 1 ni 2.
    else:
        print("Opción incorrecta.")
        print("Perdiste el turno por distraerte viendo memes.")

    # Antes de atacar, verificamos si el villano sigue con vida.
    if vida_villano > 0:

        # Generamos el ataque aleatorio del villano.
        ataque_villano = random.randint(4, 10)

        # Restamos el daño a la vida del héroe.
        vida_heroe = vida_heroe - ataque_villano

#VILLANO
        with open("historial_ataques.txt", "a") as archivo:
            archivo.write(f"Villano: {ataque_villano}\n")

        print("El villano causó", ataque_villano, "puntos de daño.")


# Mostramos el resultado de la batalla.
print()
print("=== FIN DE LA BATALLA ===")

if vida_heroe > 0:
    print("¡El héroe ganó la batalla!")

else:
    print("El villano ganó la batalla.")


# Mostramos los ataques realizados por el héroe.
print()
print("Ataques realizados por el héroe:")

for ataque in historial_ataques:
    print(ataque, end=" ")

print()