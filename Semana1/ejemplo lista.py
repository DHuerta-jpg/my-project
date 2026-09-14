nombres = []
while True:
    nombre = input("Nombre o FIN: ").strip()
    if nombre.upper() == "FIN":
        break
    if nombre == "":
        continue
nombres.append(nombre)