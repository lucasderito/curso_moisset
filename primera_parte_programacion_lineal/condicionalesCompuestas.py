'''confeccionar un programa que lea por teclado 3 numeros enteros distintos y nos muestre el mayor
utilizando el condicional ==========AND========== '''

n1 = int(input("Ingrese el primer numero :"))
n2 = int(input("Ingrese el segundo numero :"))
n3 = int(input("Ingrese el tercer numero :"))
if n1>n2 and n1>n3:
    print(f"El numero {n1} es el mayor")
elif n2>n3:
    print(f"El numero {n2} es el mayor")
else:
    print(f'El numero {n3} es el mayor')

