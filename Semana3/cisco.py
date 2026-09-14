secret_number = 7

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
+================================+
""")

while True:
    n = int(input("¿Cuál es el número secreto? (del 1 al 10)"))

    if n>secret_number:
        print("jaja no es ese, intentalo de nuevo")
    elif n<secret_number:
        print("no es ese jajaja, intentalo de nuevo")
    else:
        print ("Correcto!!")
        break
#x = 1
#y = 1.0
#z = "1"
 
#if x == y:
#      print("one")
#if y == int(z):
#    print("two")
#elif x == y:
#    print("three")
#else:
#    print("four")

#print("A mi me encantan las flores...")
#print("Me gustan las amapolas, las margaritas...")
#print("¿Pero sabes qué flor son mis favoritas?\n")

#n=str(input("Adivina!: "))


#if n == "Espatifilio":
#    print("SI, ¡El Espatifilio! es la mejor planta de todos los tiempos!")
#elif n == "pelargonio":
#    print("¡Espatifilio!, ¡No pelargonio!")
#elif n == "espatifilio":
#    print("No, ¡quiero un gran Espatifilio!")
    
