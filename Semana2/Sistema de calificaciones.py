# Sistema de calificaciones
nombres = []
calificaciones = []

while True:
    print("\n==============================")
    print(" SISTEMA DE CALIFICACIONES")
    print("==============================")
    print("1. Registrar estudiante")    
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Mostrar promedio general")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("\n--- Registrar estudiante ---")
        nombre = input("Nombre del estudiante: ").strip()

        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue

        if nombre in nombres:
            print("Ese estudiante ya está registrado.")
            continue

        fila_calificaciones = []

        for unidad in range(1, 4):
            calificacion = float(input(
                "Calificación de la unidad " + str(unidad) + ": "
            ))

            while calificacion < 0 or calificacion > 10:
                print("La calificación debe estar entre 0 y 10.")
                calificacion = float(input(
                    "Escribe nuevamente la calificación: "
                ))

            fila_calificaciones.append(calificacion)

        nombres.append(nombre)
        calificaciones.append(fila_calificaciones)
        print("Estudiante registrado correctamente.")

    elif opcion == "2":
        print("\n--- Lista de estudiantes ---")

        if len(nombres) == 0:
            print("Todavía no hay estudiantes registrados.")
        else:
            for posicion in range(len(nombres)):
                suma = 0

                for calificacion in calificaciones[posicion]:
                    suma += calificacion

                promedio = suma / len(calificaciones[posicion])

                if promedio >= 6:
                    estado = "Aprobado"
                else:
                    estado = "No aprobado"

                print("\nEstudiante:", nombres[posicion])
                print("Calificaciones:", calificaciones[posicion])
                print("Promedio:", round(promedio, 2))
                print("Estado:", estado)

    elif opcion == "3":
        print("\n--- Buscar estudiante ---")

        if len(nombres) == 0:
            print("No hay estudiantes registrados.")
            continue

        nombre_buscado = input("Nombre que deseas buscar: ").strip()
        encontrado = False

        for posicion in range(len(nombres)):
            if nombres[posicion].lower() == nombre_buscado.lower():
                suma = 0

                for calificacion in calificaciones[posicion]:
                    suma += calificacion

                promedio = suma / len(calificaciones[posicion])

                print("\nEstudiante encontrado.")
                print("Nombre:", nombres[posicion])
                print("Calificaciones:", calificaciones[posicion])
                print("Promedio:", round(promedio, 2))
                encontrado = True
                break

        if encontrado == False:
            print("El estudiante no está registrado.")

    elif opcion == "4":
        print("\n--- Promedio general ---")

        if len(calificaciones) == 0:
            print("No hay calificaciones para calcular el promedio.")
        else:
            total_calificaciones = 0
            cantidad_calificaciones = 0

            for fila in calificaciones:
                for calificacion in fila:
                    total_calificaciones += calificacion
                    cantidad_calificaciones += 1

            promedio_general = total_calificaciones / cantidad_calificaciones
            print("Promedio general:", round(promedio_general, 2))

    elif opcion == "5":
        print("Programa finalizado. ¡Buen trabajo!")
        break

    else:
        print("Opción inválida. Selecciona una opción del 1 al 5.")