# Programa para calcular el promedio

nombre = input("Escribe el nombre del estudiante: ")

calificacion1 = int(input("Primera calificación: "))
calificacion2 = int(input("Segunda calificación: "))
calificacion3 = int(input("Tercera calificación: "))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

print(f"Estudiante:  {nombre}")
print(f"Promedio:  {promedio:.2f}")

if promedio >= 6:
    print("Resultado: Aprobado")
else:
    print("Resultado: Reprobado")