#piedra papel o tijera
import random

print("===Piedra, Papel o Tijera===")
print("")
opciones = ["piedra", "papel", "tijera"]
computadora = random.choice(opciones)

print("Tu turno:\n"
"1. Piedra\n" \
"2. Papel\n" \
"3. Tijera")
turno_jugador= int(input("Elige piedra: 1, papel: 2 o tijera: 3: "))

