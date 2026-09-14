#RANDOM
import random
tiro=1
while True:
    dado= random.randint(1,6)
    print(f"Tiro {tiro}:{dado}")

    if dado==6:
        print("Juego terminado")
        break
    tiro+=1