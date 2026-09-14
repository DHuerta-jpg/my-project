nombre = "Ana"
puntos = 40

with open("historial.txt", "a") as archivo:
    archivo.write(f"{nombre}: {puntos} puntos\n")