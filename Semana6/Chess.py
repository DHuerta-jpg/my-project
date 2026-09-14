# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

for row in table:
    print(" ".join(row))
#print(table)
#print(table[0][0])  # output: ':('
#print(table[0][3])  # output: ':)'


