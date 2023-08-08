'''se cargan por teclado tres numeros distintos
mostrar por pantalla el mayor de ellos'''

n1 = int(input("Ingrese el primer numero :"))
n2 = int(input("Ingrese el segundo numero :"))
n3: int = int(input("Ingrese el tercer numero :"))
if n1 > n2 and n1 > n3:
    print(f"El numero mayor es {n1}")
else:
    if n2 > n1 and n2 > n3:
        print(f"El numero mayor es {n2}")
    else:
        print(f"El numero mayor es {n3}")
