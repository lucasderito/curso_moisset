'''dada una lista de tres valores numericos distintos se calcule e informe su rango de variacion
(se debe mostrar el mayor y menor de ellos ) '''

n1 = int(input("Ingrese el primer numero :"))
n2 = int(input("Ingrese el segundo numero :"))
n3 = int(input("Ingrese el tercer numero :"))

if n1 > n2 and n1 > n3:
    print(f"El numero mayor es el primero :{n1}")
elif n2 > n1 and n2 > n3:
    print(f"El numero mayor es el segundo :{n2}")
else:
    print(f"El numero mayor es el tercero :{n3}")

if n1 < n2 and n1 < n3:
    print(f"El numero menor es el primero :{n1}")
elif n2 < n1 and n2 < n3:
    print(f"El numero menor es el segundo :{n2}")
else:
    print(f"El numero menor es el tercero :{n3}")
