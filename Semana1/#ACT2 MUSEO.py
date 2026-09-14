#ACT2 MUSEO
total=0
contador=0

total_visitantes=(int(input("¿Cuántos visitantes ingresarán al museo? ")))
#Uso de break
if total_visitantes<=0:
    print("Número de visitantes inválido. Cancelado")
else:
    while contador < total_visitantes:
        print(f"\nVisitante {contador+1} ---")
    #¿Es menor de 3 años?
    menor=input("¿El visitante es menor de 3 años? (s/n): ")
    