'''se ingresa por teclado un numero positivo de 1 o 2 digitos 1 - 99 mostrar un mensaje indicando
si el numero tiene 1 o dos digitos'''

numero = int(input("ingrese el numero de uno o dos digitos :"))
if numero < 10:
    print("el numero tiene 1 digito")
elif numero > 9 and numero <= 99:
    print("el numero tiene 2 digitos")
else:
    print("el numero tiene mas de dos digitos")
