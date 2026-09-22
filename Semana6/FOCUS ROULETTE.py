import random
import time

tareas = []
hobbies = []


#OPCION 1
def agregar_tarea():
    print("\n--- REGISTRAR TAREA ---")
    #Selección de categoría
    print("\nSelecciona la categoria:")
    print("1. Urgente")
    print("2. Trabajo para la semana")
    print("3. Hobbies")
    categoria_opcion = input("Opcion (1-3): ").strip()

    while categoria_opcion not in ["1", "2", "3"]:
        print("ERROR: Categoria invalida.")
        categoria_opcion = input("Opcion (1-3): ").strip()

    if categoria_opcion == "1":
        categoria = "Urgente"
    elif categoria_opcion == "2":
        categoria = "Tarea para la semana"
    else:
        categoria = "Hobbie"

    #Se solicita la tarea
    nombre_tarea = input("\nIngresa la tarea pendiente: ").strip()

    if nombre_tarea == "":
        print("ERROR: No se puede agregar una tarea vacia.")
        return

    #Limitar el número de caracteres por tarea agregando puntos suspensivos....
    if len(nombre_tarea) > 30:
        nombre_tarea = nombre_tarea[:27] + "..."

    # Validar si el nombre ya existe recorriendo la lista de diccionarios
    for t in tareas:
        if t["nombre"] == nombre_tarea:
            print("ERROR: La tarea ya esta en la lista.")
            return

    #Guardamos la tarea como un diccionario dentro de la lista
    nueva_tarea = {"nombre": nombre_tarea, "categoria": categoria}
    tareas.append(nueva_tarea)
    print(">>> TAREA GUARDADA CON EXITO <<<")

#Función para imprimir tabla
def print_tabla(nested_list, column_names):
    col_widths = [len(str(col)) for col in column_names]
    for row in nested_list:
        for i, item in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(item)))

    header_row = "| " + " | ".join(f"{str(val):<{col_widths[i]}}" for i, val in enumerate(column_names)) + " |"
    divider = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

    print(divider)
    print(header_row)
    print(divider)

    for row in nested_list:
        row_str = "| " + " | ".join(f"{str(val):<{col_widths[i]}}" for i, val in enumerate(row)) + " |"
        print(row_str)

    print(divider)

#OPCION 2:
def mostrar_tareas():
    print("\n--- Tareas Pendientes ---")
    if len(tareas) == 0:
        print(">>> No hay tareas pendientes.")
    else:
        tabla_datos = [[i + 1, tarea["nombre"], tarea["categoria"]] for i, tarea in enumerate(tareas)]
        print_tabla(tabla_datos, ["#", "Tarea", "Categoria"])

#OPCION 3:
def girar_ruletas():
    print("\n--- RULETA DE ENFOQUE ---")

    #Separar tareas por su categoria para alimentar 2 ruletas distintas
    urgentes = [t["nombre"] for t in tareas if t["categoria"] == "Urgente"]
    semanales = [t["nombre"] for t in tareas if t["categoria"] == "Tarea para la semana"]


    if len(urgentes) == 0 and len(semanales) == 0:
        print(">>> No hay tareas registradas para girar la ruleta.")
        return

    print("\nGirando ruletas de Enfoque...\n")
    
    #el coso del tiempo
    vueltas = 15
    tiempo = 0.05

    ganador_urgente = "Sin Urgentes"
    ganador_semanal = "Sin Semanales"

    for i in range(vueltas):
        #Se muesta la tarea aleatoria
        if len(urgentes) > 0:
            ganador_urgente = random.choice(urgentes)

        #selección aleatoria para la animacion
        if len(semanales) > 0:
            ganador_semanal = random.choice(semanales)

        #si el número de caracteres es mayor a 15 se recorta y se agregan puntos suspensivos
        if len(ganador_urgente) > 15:
            rul_u = ganador_urgente[:12] + "..."
        else:
            rul_u = ganador_urgente


        if len(ganador_semanal) > 15:
            rul_s = ganador_semanal[:12] + "..."
        else:
            rul_s = ganador_semanal

        #.ljust() para rellenar espacios
        res_u = f"Urgente: [ {rul_u} ]".ljust(21)
        res_s = f"Semanal: [ {rul_s} ]".ljust(21)

        #Animacion para la ruleta, Flush = True para mostrar el texto
        print(f"\r {res_u}   |    {res_s}",end="", flush=True)
        time.sleep(tiempo)
        tiempo += 0.01

  

    #Impresion de resultados finales
    print("\n\n==================================================")
    print("  RESULTADOS DE LA RULETA  ")
    print("==================================================")
    print(f" Tarea Urgente: {ganador_urgente}")
    print(f" Tarea Semanal: {ganador_semanal}")
    print("--------------------------------------------------")
    print("\033[2mAhora puedes hacer estas asignaciones\033[0m")
    print("\033[2m¡Cuando las hayas terminado, no olvides marcarlas como completadas!\033[0m")
    print("==================================================\n")

#OPCIÓN 4
def completar_tareas():
    print("\n--- Completar Tarea ---")
    if len(tareas) == 0:
        print(">>> No hay tareas que eliminar...")
        return
    
    mostrar_tareas()

    opcion=input("Ingresa el número de la tarea completada: ").strip()
    #el isdigit para saber si el texto contiene solo números
    if not opcion.isdigit():
        print("ERROR: Ingresa un número válido.")
        return

    num = int(opcion)

    #Para confirmar la eliminacion de tarea
    #validar que el número exista en la lista
    if 1 <= num <= len(tareas):
        confirmar = input(f"¿Seguro de completar '{tareas[num - 1]['nombre']}'? (s/n):").strip().lower()

        if confirmar == "s":
            tarea_eliminada = tareas.pop(num -1)
            
            #Guardar Tareas completadas con encoding=utf-8 
            with open("tareas_completadas.txt","a", encoding="utf-8") as archivo:
                archivo.write(f"{tarea_eliminada['nombre']} | Categoría: {tarea_eliminada['categoria']}\n")
            print(f"¡¡¡TAREA '{tarea_eliminada['nombre']}' COMPLETADA CON ÉXITO!!!")

            hobbies_lista = [t["nombre"] for t in tareas if t["categoria"] == "Hobbie"]

            if len(hobbies_lista) == 0:
             print(">>>¡Agrega un Hobbie para seleccionar una recompensa!")
            else:
             print("\nGirando ruleta de recompensa...\n")

             #animacion de vueltas para ruleta
             vueltas = 15
             tiempo = 0.05
             for i in range(vueltas):
                hobbie_recompensa = random.choice(hobbies_lista) 

                if len(hobbie_recompensa) > 18:
                    rul_h = hobbie_recompensa[:15] + "..." 
                else: 
                    rul_h = hobbie_recompensa


                #flush=true para mostrar el texto     
                print(f"\r  Hobbie: [ {rul_h} ]".ljust(35), end="", flush=True)
                time.sleep(tiempo)
                tiempo += 0.01

             print("\n\n==================================================")
             print(f"  RECOMPENSA DE HOBBIE: Se te asignó un hobbie al azar!")
             print(f"  ----> {hobbie_recompensa}")
             print("==================================================\n")
        else:
            print("¡Operación cancelada!")
    else:
        print("ERROR: El número no existe en la lista")

#Menu del programa
while True:
    print("\n=========================")
    print(" FocusRoulette - Asistente de Enfoque")
    print("\033[2mRegistrar, clasificar y elegir tareas pendientes\033[0m")
    print("=========================")
    print("1. Agregar Tarea pendiente")
    print("2. Ver lista de Tareas pendientes")
    print("3. ¡Girar la ruleta!")
    print("4. Completar Tarea")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ").strip()

    while opcion not in ["1", "2", "3", "4", "5"]:
        print("ERROR: Opción inválida. Por favor, selecciona una opción válida (1-5).")
        opcion = input("Selecciona una opción (1-5): ").strip()

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        girar_ruletas()
    elif opcion == "4":
        completar_tareas()
    elif opcion == "5":
        print("\n ¡Eso es todo, amigos!")
        break