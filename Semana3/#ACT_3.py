#ACT_3
tabla=[]
#Creas tu poderosa fila de base, con rango
for numero_fila in range(1, 11):
    #filita vacía para almacenar los resultados
    nueva_fila=[]
    #la variable de "acumulador"
    resultado=0
    #recorrer posiciones de fila
    for columna in range(1, 11):
        #Se suman sin usar el operador  
        resultado=resultado+numero_fila
        #se agrega cada fila hasta que termine el for
        nueva_fila.append(resultado)
        #se agrega la fila a la tablita (matriz)
    tabla.append(nueva_fila)  


#presentación de la tabla
print("==========================================")
print("Tabla Pitagórica")
#ordenar la tabla
for nueva_fila in range(0,10):
    for columna in range(0,10):
        print(f"| {tabla[nueva_fila][columna]} |", end="")
    print()
print("==========================================")

#inputs
no_uno=int(input("Ingrese el primer número: "))
no_dos=int(input("Ingrese el segundo número: "))

print("==========================================")
print(f"El resultado es: {tabla[no_uno-1][no_dos-1]}")
print("==========================================")