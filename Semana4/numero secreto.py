import random

numero_secreto=random.randint(1,10)
intentos=0
numero=0



while numero!=numero_secreto and intentos<5:
    numero=int(input("Adivina el numero secreto: "))
    if numero>numero_secreto:
        print(f"El numero {numero} es mayor que el secreto")
    elif numero<numero_secreto:
        print(f"El numero {numero} es menor que el secreto")
    else:
         print(f"¡Felicidades! Has adivinado el numero secreto")

    intentos=intentos+1
    print("----------------------------------")
    print(f"Intentos: {intentos}")
    print("----------------------------------")

if intentos==5:
    print("Has agotado tus intentos.")
    print(f"El numero secreto era: {numero_secreto}")