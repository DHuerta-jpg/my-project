dibujos = [
    [
        "  _______",
        "  |     |",
        "  |",
        "  |",
        "  |",
        "  |",
        "========="
    ],
    [
        "  _______",
        "  |     |",
        "  |     O",
        "  |",
        "  |",
        "  |",
        "========="
    ],
    [
        "  _______",
        "  |     |",
        "  |     O",
        "  |     |",
        "  |",
        "  |",
        "========="
    ],
    [
        "  _______",
        "  |     |",
        "  |     O",
        "  |    /|",
        "  |",
        "  |",
        "========="
    ],
    [
        "  _______",
        "  |     |",
        "  |     O",
        "  |    /|\\",
        "  |",
        "  |",
        "========="
    ],
    [
        "  _______",
        "  |     |",
        "  |     O",
        "  |    /|\\",
        "  |    /",
        "  |",
        "========="
    ],
    [
        "  _______",
        "  |     |",
        "  |     O",
        "  |    /|\\",
        "  |    / \\",
        "  |",
        "========="
    ]
]

#funcion para mostrar el dibujo
def mostrar_dibujo(numero_errores):

  dibujo_actual=dibujos[numero_errores]
  for linea in dibujo_actual:
      print(linea)
#Almacena la palabra a descubrir
palabra_secreta=["a","r","r","o","z"]

#imprime la letras encontradas
palabra_visible=["_","_","_","_","_"]

letras_utilizadas=[]

vidas=6

errores=0

#inicio el ciclo del juego
while True:
  print()
  mostrar_dibujo(errores)
  print("Palabra:",end=" ")
  for letra in palabra_visible:
    print(letra,end=" ")
  print()
  print("Letras utilizadas:",end=" ")
  for letra in letras_utilizadas:
    print(letra,end=" ")
  print()
  print(f"Vidas {vidas}")
  print(f"Errores {errores}")  
  
  intento=input("Ingresa una letra: ")
  letras_utilizadas.append(intento)

  #valido que la letra exista y se reemplace en mi lista visible
  if intento in palabra_secreta:
    for i in range(len(palabra_secreta)):
      if intento==palabra_secreta[i]:
        palabra_visible[i]=intento
  else:
    errores=errores+1
    vidas=vidas-1

  if vidas==0:
    print("Perdiste")
    break

  if palabra_visible==palabra_secreta:
    print("Ganaste")
    break
