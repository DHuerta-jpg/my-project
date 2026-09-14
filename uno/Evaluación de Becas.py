nombre=input("Ingresa tu nombre: ")
promedio=(int(input("Promedio: ")))
vigencia=input("¿Eres estudiante vigente?: (s/n)")
ingreso=(int(input("¿De cuánto es tu ingreso?: $")))
 
if promedio>=0 and promedio<=100:
  if promedio>=95 and vigencia.lower()=="s":
    print("Obtienes beca del 50%")
  elif promedio>=85 and ingreso<=15000:
      print("Obtienes beca del 25%")
  else:
        print("No consigues beca")
else:
  print("Promedio No válido")

print("======Resultado de Evaluación=====\n")
print(f"Nombre del estudiante: {nombre}")
print(f"Promedio del estudiante:{promedio}")
print(f"Ingreso Familiar del estudiante:{ingreso}")
print(f"Estudiante vigente:{vigencia}")