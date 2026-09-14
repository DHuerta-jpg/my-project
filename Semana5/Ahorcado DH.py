#Ahorcado
import random

dibujos = [
    [
        "  _______",
        "  |     |",
        "  |",
        "  |",
        "  |",
        "  |",
        "========="
    ],
    [
        "  _______",
        "  |     |",
        "  |     O",
        "  |",
        "  |",
        "  |",
        "========="
    ],
    [
        "  _______",
        "  |     |",
        "  |     O",
        "  |     |",
        "  |",
        "  |",
        "========="
    ],
    [
        "  _______",
        "  |     |",
        "  |     O",
        "  |    /|",
        "  |",
        "  |",
        "========="
    ],
    [
        "  _______",
        "  |     |",
        "  |     O",
        "  |    /|\\",
        "  |",
        "  |",
        "========="
    ],
    [
        "  _______",
        "  |     |",
        "  |     O",
        "  |    /|\\",
        "  |    /",
        "  |",
        "========="
    ],
    [
        "  _______",
        "  |     |",
        "  |     O",
        "  |    /|\\",
        "  |    / \\",
        "  |",
        "========="
    ]
]

#para mostrar el dibujo
def mostrar_dibujo(errores):
    dibujo_actual = dibujos[errores]
    for linea in dibujo_actual:
        print(linea)

#Guardar intentos en archivo
def guardar_partida(palabra_secreta, resultado, intento):
    with open("historial_intentos.txt","a") as archivo:
            archivo.write("=================================\n")
            archivo.write(f"Palabra secreta: {palabra_secreta}\n")
            archivo.write(f"Resultado: {resultado}\n")
            archivo.write(f"Intentos realizados: {','.join(intento)}\n")
            archivo.write("=================================\n")

#Partida Completa
def jugar():
    #selecciona palabra random, remplaza el número de letras con "_" y guarda una lista vacía de letras adivinadas
    palabra_secreta = random.choice(["arroz", "rosa", "agua", "oso", "zorro", "casa", "leche", "trabajo", "camino", "corazon"])
    palabra_visible = ["_"] * len(palabra_secreta)
    letras_adivinadas = []
    vidas = 6
    errores = 0

    #inicia el turno, llama a las imágenes según los errores
    while True:
        print()
        mostrar_dibujo(errores)
        #para mostrar las palabras correctas, el end= es para que no haya saltos de linea 
        print("Palabra:", end=" ")
        for letra in palabra_visible:
            print(letra, end=" ")
        print()
        #muestra intentos, vidas y errores
        print("Letras utilizadas:", end=" ")
        for letra in letras_adivinadas:
            print(letra, end=" ")
        print()
        print(f"Vidas restantes: {vidas}")
        print(f"Errores: {errores}")

        #para ver los intentos, los pone en minúscula y guarda las correctas en lista
        intento = input("Ingresa una letra: ").lower()
        letras_adivinadas.append(intento)

        #recorre la palabra por el índice i y si coincide con la posición reemplaza _ por letra
        if intento in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if intento == palabra_secreta[i]:
                    palabra_visible[i] = intento 
        #else, si no le atina, te muestran vidas restantes (se resta 1) y suma a tus errores
        else:
            errores += 1
            vidas -= 1
            print(f"Letra incorrecta. Te quedan {vidas} vidas.")
    #romper el bucle con el break 
        #cuando te quedes sin vida el juego te muestra la palabra y guardar datos en el historial   
        if vidas == 0:
            print("¡Has perdido! La palabra era..... ","".join(palabra_secreta))
            guardar_partida(palabra_secreta, "Derrota", letras_adivinadas)
            break

        #cuando ganes se muestra la palabra y se guarda la victoria en el archivo
        #el join es para que se muestre el texto continuo        
        if "".join(palabra_visible) == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra:", "".join(palabra_secreta))
            guardar_partida(palabra_secreta, "Victoria", letras_adivinadas)
            break

#define el menú principal del juego
def main():
    print("===============================")
    print("--------Ahorcado--------")
    while True:
        #si se responde "s" se llama el turno a jugar, si no, se termina el juego con break
        jugar()
        opcion = input("¿Deseas jugar otra vez? (s/n): ").lower()
        if opcion != "s":
            print("================================")
            print("Gracias por jugar. ¡Hasta luego!")
            break
main()