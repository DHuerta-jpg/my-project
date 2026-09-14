def imprimir_tabla(matriz):
    for fila in matriz:
        for numero in fila:
            print(f"{numero:4}", end="")
        print()  # salto de línea al terminar cada fila
def crear_matriz(n):
    return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]

tabla = crear_matriz(10)
imprimir_tabla(tabla)