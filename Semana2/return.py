def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

bandera = 0
while bandera!=2:
    numero=int(input("ingrese un número para generar su tabla de multiplicar: "))
    tabla_multiplicar(numero)
    opcion=input("¿Desea generar otra tabla de multiplicar? (Sí, No): ")
    if opcion=="no" or opcion=="n":
        bandera=2
        print("Gracias por usar el programa.")