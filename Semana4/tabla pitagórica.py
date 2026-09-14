from Semana4.matrizact3 import imprimir_tabla


def crear_matriz(n):
    matriz = []
    for i in range(1, n + 1):
        fila = []
        for j in range(1, n + 1):
            fila.append(i * j)
        matriz.append(fila)
    return matriz
tabla = crear_matriz(10)
imprimir_tabla(tabla)