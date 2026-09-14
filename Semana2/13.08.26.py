compra=float(input("Total de compra: $"))
membresia=input("¿Tiene membrasía? (s/n):")

#METODOS ":lower()"
if compra>=1000 and membresia.lower()=="s":
  descuento=(compra*0.15)
else:
  descuento= 0

total=(compra-descuento)
print("Total a pagar: $", total)