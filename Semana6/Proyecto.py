import random
import time

tareas = []
hobbies = []


#OPCION 1
def agregar_tarea():
    print("\n--- [REGISTRAR TAREA] ---")
    #Selección de categoría
    print("\nSelecciona la categoria:")
    print("1. Urgente")
    print("2. Trabajo para la semana")
    print("3. Hobbies")
    categoria_opcion = input("Opcion (1-3): ").strip()

    while categoria_opcion not in ["1", "2", "3"]:
        print(">>> ERROR: Categoria invalida.")
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
        print(">>> ERROR: No se puede agregar una tarea vacia.")
        return

    # Validar si el nombre ya existe recorriendo la lista de diccionarios
    for t in tareas:
        if t["nombre"] == nombre_tarea:
            print(">>> ERROR: La tarea ya esta en la lista.")
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
    print("\n--- [TAREAS PENDIENTES] ---")
    if len(tareas) == 0:
        print(">>> No hay tareas pendientes.")
    else:
        tabla_datos = [[i + 1, tarea["nombre"], tarea["categoria"]] for i, tarea in enumerate(tareas)]
        print_tabla(tabla_datos, ["#", "Tarea", "Categoria"])


#OPCION 3:
def girar_ruletas():
    print("\n--- [RULETA DE ENFOQUE] ---")

    #Separar tareas por su categoria para alimentar 2 ruletas distintas
    urgentes = [t["nombre"] for t in tareas if t["categoria"] == "Urgente"]
    semanales = [t["nombre"] for t in tareas if t["categoria"] == "Tarea para la semana"]
    hobbies = [t["nombre"] for t in tareas if t["categoria"] == "Hobbies"]


    if len(urgentes) == 0 and len(semanales) == 0:
        print(">>> No hay tareas registradas para girar la ruleta.")
        return

    print("\nGirando ruletas de Enfoque...\n")
    
    #sleep
    vueltas = 15
    tiempo = 0.05
    for i in range(vueltas):
        # Muestra una opcion aleatoria si existe, o un texto por defecto
        temp_urgente = random.choice(urgentes) if len(urgentes) > 0 else "Sin urgentes"
        temp_semanal = random.choice(semanales) if len(semanales) > 0 else "Sin semanales"
        temp_hobbies = random.choice(hobbies) if len(hobbies) > 0 else "Sin hobbies"

        
        print(f"\r  Urgente: [ {temp_urgente} ]   |   Semanal: [ {temp_semanal} ],",end="", flush=True)
        time.sleep(tiempo)
        tiempo += 0.01

    #Seleccion final real
    ganador_urgente = random.choice(urgentes) if len(urgentes) > 0 else "Ninguna registrada"
    ganador_semanal = random.choice(semanales) if len(semanales) > 0 else "Ninguna registrada"
    
    #Hobbie instantaneo
    hobbie_recompensa = random.choice(hobbies)

    #Impresion de resultados finales
    print("\n\n==================================================")
    print("  RESULTADOS DE TU SESION DE ENFOQUE")
    print("==================================================")
    print(f"  * Tarea Urgente seleccionada: {ganador_urgente}")
    print(f"  * Tarea Semanal seleccionada: {ganador_semanal}")
    print("--------------------------------------------------")
    print(f"  RECOMPENSA DE HOBBIE (Instantaneo):")
    print(f"    -> {hobbie_recompensa}")
    print("==================================================\n")


#Menu del programa
while True:
    print("\n=========================")
    print(" FocusRoulette - Asistente de Enfoque")
    print("=========================")
    print("1. Agregar Tarea pendiente")
    print("2. Ver lista de Tareas pendientes")
    print("3. ¡Girar la ruleta!")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ").strip()

    while opcion not in ["1", "2", "3", "4"]:
        print(">>> ERROR: Opción inválida. Por favor, selecciona una opción válida (1-4).")
        opcion = input("Selecciona una opción (1-4): ").strip()

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        girar_ruletas()
    elif opcion == "4":
        print("\n ¡Programa finalizado!")
        break