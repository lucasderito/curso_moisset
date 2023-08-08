'''se ingresan por teclado tres numeros si todos los valores ingresados son menores a 10
imprimir en pantalla , todos los numeros son menores a 10 '''

n1 = int(input("Ingrese el primer numero :"))
n2 = int(input("Ingrese el segundo numero :"))
n3 = int(input("Ingrese el tercer numero :"))
if n1 < 10 and n2 < 10 and n3 < 10:
    print("TODOS los  numeros ingresados son menores a 10")
else:
    print("NO TODOS los numeros ingresados menores a 10")

