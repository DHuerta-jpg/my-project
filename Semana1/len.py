lista=[1,2,3,4]
print(len(lista))

lista.append("probar")
print(len(lista))

multiplos=[]
for numero in range(3,1001,3):
    multiplos.append(numero)
print(len(multiplos))#333
print(multiplos[-1])#999
#print(multiplos)


productos=["teclado", "mouse"]
print("inicio", productos)
#.append
productos.append("monitor")
print("append:", productos)
#.insert
productos.insert(1, "webcam")
print("insert:", productos)
#.remove
productos.remove("mouse")
print("remove:", productos)
#.pop
eliminado=productos.pop(0)
print("pop:", eliminado, productos)
#.reverse
productos.reverse()
print("reverse:", productos)
#.sort
productos.sort()
print("sort:", productos)