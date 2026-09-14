def crear_tabla(n):
    tabla = [] #Crea lista vacía para las filas
    for i in range(1, n + 1): #i, recorre 1, 2, 3...,n
        fila = [] #lista vacia para fila
        for s in range(1, n + 1): #s recorre 1, 2, 3...,n
            fila.append(i*s) #Agrega el producto de i y s a la fila
        tabla.append(fila) #Agrega la fila a la tabla
    return tabla

def imprimir_tabla(tabla):
    for fila in tabla: #Recorre cada fila de la tabla
        for numero in fila: #Recorre cada número de la fila
            print(f"{numero:4}", end="") #Imprime el número con un ancho de 4 caracteres
        print() #Salto de línea al terminar cada fila

def multiplicar(tabla,num1,num2):
    return tabla[num1 - 1][num2 - 1] #devuelve el resultado usando la tabla


tabla = crear_tabla(10) #Crea la tabla de multiplicar del 1 al 10
imprimir_tabla(tabla)

num1 = int(input("Ingresa el primer número (1-10):"))
num2 = int(input("Ingresa el segundo número (1-10):"))

resultado = multiplicar(tabla,num1,num2) #Llama a la función multiplicar para el resultado
print(f"El resultado de {num1} x {num2} es: {resultado}")
