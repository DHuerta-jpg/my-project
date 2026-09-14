inventario = [["Teclado", 12], ["Mouse", 20], ["Monitor", 7]]
inventario.append(["Webcam", 5]) # 1 append
inventario.insert(1, ["USB", 30]) # 2 insert
inventario.remove(["Monitor", 7]) # 3 remove
eliminada = inventario.pop(0) # 4 pop
inventario.reverse() # 5 reverse
inventario.sort() # 6 sort
print("Matriz final:", inventario)
print("Fila eliminada:", eliminada)


#Buscar dentro de una matriz
calificaciones = [[79, "Rosa"],
[94, "Juan"],
[100, "Lalo"]]
hay_cien = False
notas = []
for fila in calificaciones:
    notas.append(fila[0])
    if fila[0] == 100:
        hay_cien = True

print(f"\t Calificaciones: {notas}")
print("Hay alguna materia con calificación de 100: ", hay_cien)
print("Nota mínima: ", min(notas), "Nota máxima: ", max(notas))