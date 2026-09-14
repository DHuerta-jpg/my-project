tipo_visitante:list[str]=["Estudiante", "Profesor", "Adulto Mayor", "Público"]
tipo_descuento:list[float]=[0.10,0.10,0.12,0]

for x in tipo_visitante:
    print(x)
total_visitantes=int(input("Ingrese el número total de visitante: "))
total=0
contador=0

while contador < total_visitantes:
    edad=int(input("Ingrese la edad del visitante: "))

    if edad<-1:
        print("Nombre no válido")
        break
    if edad<=3:
        print(f"El visitante es un {tipo_visitante[0]} y no paga entrada")
        precio_base=0
    elif edad<18:
        print(f"El visitante es un {tipo_visitante[0]} y paga entrada con un descuento del {tipo_descuento[0]*100}%")
        precio_base=30
    elif edad>=18:
        print(f"El visitante es un {tipo_visitante[3]} y paga entrada con un descuento del {tipo_descuento[3]*100}%")
        precio_base=45
    else:
        print("Edad Inválida")
        break
    print("\n Tipo de visitantes")
    for posicion in range(len(tipo_visitante)):
        print(f"{posicion+1}. {tipo_visitante[posicion]} con un descuento del {tipo_descuento[posicion]*100}%")
    opcion=int(input("Ingrese el tipo de visitante: "))
    contador+=1