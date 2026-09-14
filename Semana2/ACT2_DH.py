total = 0
contador = 0
total_visitantes = int(input("¿Cuántos visitantes pagarán boleto?: "))

if total_visitantes <= 0:
    print("Número de visitantes inválido. Cancelado.")
else:
    while contador < total_visitantes:
        print(f"\t--- Visitante {contador + 1} ---")
        #3 años
        menor = input("¿Es menor de 3 años? (s/n): ")

        if menor == "s":
            print("No paga boleto.")
            contador += 1
            continue

        #mayor de edad
        mayor_edad = input("¿Es mayor de edad? (s/n): ")

        if mayor_edad == "s":
            precio = 45
        else:
            precio = 30

        #menú
        print("Tipo de visitante:")
        print("1. Adulto mayor")
        print("2. Profesor")
        print("3. Estudiante")
        print("4. Público general")
        opcion = int(input("Ingrese una opción (1-4): "))

        #if
        adulto_mayor = False
        profesor = False
        estudiante = False

        if opcion == 1:
            adulto_mayor = True
        elif opcion == 2:
            profesor = True
        elif opcion == 3:
            estudiante = True
        elif opcion == 4:
            pass
        else:
            print("Opción inválida.")
            contador += 1
            continue

        #descuentito
        if adulto_mayor:
            descuento = 0.12
        elif profesor:
            descuento = 0.10
        elif estudiante:
            descuento = 0.10
        else:
            descuento = 0.0

        #precio final y suma
        precio_final = precio - (precio * descuento)
        total += precio_final

        print(f"\nPrecio base: ${precio}, Descuento: {descuento*100}%, Precio final: ${precio_final:.2f}")

        contador += 1
    print(f"\tTotal a pagar por todos los visitantes: ${total:.2f}")
    print(f"\t--- Gracias por su visita, vuelva pronto. :) ---")