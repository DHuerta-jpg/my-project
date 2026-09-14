#directa
m1=[[7, 7], [7, 7], [7, 7]]


#ciclos
m2 = []
#filas
for f in range(3):
    m2.append([])
    #columnas
    for c in range(2):
        m2[f].append(10)
print(m2)

#compresion
m3 = [[7 for c in range(2)]
      for f in range(3)]

#print(m3)

paquetes = [["Start", "Pro"],
            ["10 GB", "30 GB"]]
for fila in paquetes:
    for dato in fila:
        print(dato, end=" | ")
print()