'''se ingresa por teclado un valor entero , mostrar una leyenda que indique si el numero es positivo
negativo o nulo '''

numero = float(input("ingrese el numero :"))
if numero > 0:
    print("el numero es positivo")
elif numero < 0:
    print("el numero es negativo")
else:
    print("el numero es nulo")
