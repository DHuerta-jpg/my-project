#3 sucursales × 5 días. Totales por sucursal y día, mayor venta.
matriz=[]
for fila in range(3):
    matriz.append([])
    for columna in range(5):
        matriz[fila].append(0)
#print(matriz)

for fila in matriz:
    for columna in fila:
        print(columna, end=" | ")
    print("\n")