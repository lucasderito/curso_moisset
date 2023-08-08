'''confeccionar un programa que permita cargar un numero entero de hasta tres cifras y muestre
un mensaje indicando si tiene 1 , 2 o 3 cifras . Mostrar un mensaje de error si el numero de cifras es mayor'''

numero = int(input("ingrese un numero entero de hasta 3 cifras :"))
if numero <= 10:
    print("el numero tiene 1 cifra")
elif numero < 100:
    print("el numero tiene 2 cifras")
elif numero < 1000:
    print("el numero tiene 3 cifras")
else:
    print("error , el numero ingresado tiene mas de 3 cifras")
