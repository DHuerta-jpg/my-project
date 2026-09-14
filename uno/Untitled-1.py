terminacion=int(input("Placa: "))
terminacion_0=0
terminacion_1=0
terminacion_2=0
terminacion_9=0

while terminacion>=0:
    if terminacion==0:
     terminacion_0+=1
    elif terminacion==1:
        terminacion_1+=1
    elif terminacion==2:
        terminacion_2+=1
    elif terminacion==9:
        terminacion_9+=1
    else:
     print("Dato no valido")
    terminacion=int(input("Dame terminación Placa"))
print(f"Total de placas terminación 0: {terminacion_0}")
print(f"Total de placas terminación 1: {terminacion_1}")
print(f"Total de placas terminación 2: {terminacion_2}")
print(f"Total de placas terminación 9: {terminacion_9}")