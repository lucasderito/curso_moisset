'''se ingresan tres valores por teclado si todos son iguales se imprimen la suma del primero con el segundo
y a este resultado se lo multiplica por el tercero'''

n1 = int(input("Ingrese el primer numero :"))
n2 = int(input("Ingrese el segundo numero :"))
n3 = int(input("Ingrese el tercer numero :"))
if n1 == n2 and n1 == n3:
    operacion = (n1 + n2) * n3
    print(f"el resultado seria {operacion}")
else:
    print("No se cumple la condicion del enunciado")
