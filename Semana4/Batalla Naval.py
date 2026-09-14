# Batalla Naval

import random

# Juego
def jugar():
    posicion_barco = random.randint (0,4)

    # Primero creas tus listas y defines dónde está el barco.
    oceano = ["agua", "agua", "agua", "agua", "agua"]
    oceano[posicion_barco] = "Barco"

    # Limitas tus intentos y defines si el barco fue encontrado.
    intentos = 3
    barco_encontrado = False

# Mientras tengas intentos y no hayas encontrado el barco
    while intentos > 0:
        posicion = int(input("Elige una opción del 1 al 5: "))

        if posicion >= 1 and posicion <= 5:
            posicion_lista = posicion - 1
        else:
            print("La posición debe estar entre 1 y 5")
            continue
    
        if oceano[posicion_lista] == "Barco":
            print ("¡Impacto! Hundiste el barco.")
            barco_encontrado = True
            break
        else:
            print("¡Agua!")
            intentos -= 1
            print()
            print("Intentos disponibles: ", intentos)

    if barco_encontrado == False:
        print("El barco escapó.")
        print("El barco estaba en la posición: ", posicion_barco + 1)
    else:
        print("Ganaste la batalla naval!")
        

def main():
    print ("=== BATALLA NAVAL ===")
    while True:
        jugar()
        opcion = input("¿Deseas jugar otra vez? (s/n): ").lower()
        if opcion != "s":
            print("================================")
            print("Gracias por jugar. ¡Hasta luego!")
            break
main()