from random import random


tareas = []

while True:
    print("\n =========================")
    print(" FocusRoulette - Asistente de Enfoque")
    print("===========================")
    print("1. Agregar Tarea pendiente")
    print("2. Ver lista de Tareas pendientes")
    print("3. ¡Girar la ruleta!")
    print("4. Salir")
#Editar tareas

    opcion = input("Selecciona una opción (1-4): ")

    while opcion not in ["1", "2", "3", "4"]:
        print(">>> ERROR: Opción inválida. Por favor, selecciona una opción válida (1-4).")
        opcion = input("Selecciona una opción (1-4): ")

#OPCIÓN 1: Agregar tarea pendiente
    if opcion == "1":
        print("\n--- [REGISTRAR TAREA] ---")
        #registro de tarea.strip para evitar espacios en blanco 
        tarea = input("Ingresa la tarea pendiente: ").strip()

        #si no hay nada
        if tarea == "":
            print(">>>ERROR:No se puede agregar una tarea vacía.")
            continue

        #si la tarea ya existe
        if tarea in tareas:
            print(">>ERROR: La tarea ya está en la lista.")    
            continue

        #guardar en la lista
        tareas.append(tarea)
        print(">>> ¡TAREA GUARDADA CON ÉXITO! <<<")

#OPCIÓN 2: Mostrar lista de tareas pendientes
    elif opcion == "2":
        print("\n--- [TAREAS PENDIENTES] ---")

        #si no hay nada en la lista
        if len(tareas) == 0:
            print(">>> No hay tareas pendientes.")
        else:
            #Recorrer lista para mostrar las tareas 1 por 1
            for i in range(len(tareas)):
                print(f"{i + 1}. {tareas[i]}")
#OPCIÓN 3: Girar la ruleta
    elif opcion == "3":
        print("\n--- [RULETA] ---")

        #si no hay nada en la lista
        if len(tareas) == 0:
            print(">>> No hay tareas pendientes para girar la ruleta.")
            continue
        
    # Opcion_tarea =len(tareas)
     #      random_index = random.randint(0, Opcion_tarea - 1)
      #       tarea_seleccionada = tareas[random_index]  

#OPCIÓN 4: FIN
    elif opcion == "4":
        print("\n ¡Programa finalizado!")
        break