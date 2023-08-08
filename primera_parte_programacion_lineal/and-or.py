'''se ingresan por teclado tres numeros si alguno de los numerso ingresados es menor a 10
imprimir en pantalla , alguno de los numeros ingresados es menor a 10  '''


n1 = int(input("Ingrese el primer numero :"))
n2 = int(input("Ingrese el segundo numero :"))
n3 = int(input("Ingrese el tercer numero :"))
if n1 < 10 or n2 < 10 or n3 < 10:
    print("ALGUNO de los numeros ingresados es menor a 10")
else:
    print("ninguno de los numeros ingresados es menor a 10")