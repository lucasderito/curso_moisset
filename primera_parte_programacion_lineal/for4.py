''' Escribir un programa que lea 10 numeros enteros y luego muestre cuantos valores ingresados
fueron multiplos de 3 y cuantos de 5. Debemos tener en cuenta que hay numeros que son
multiplos de 3 y de 5 a la vez '''

multiplos_de_3 = 0
multiplos_de_5 = 0

for x in range(10):
    num = int(input("Ingrese un numero entero :"))
    if num % 3 == 0:
        multiplos_de_3 += 1
    if num % 5 == 0:
        multiplos_de_5 += 1
print(f"La cantidad de multiplos de 3 es de : {multiplos_de_3}")
print(f"La cantidad de multiplos de 5 es de : {multiplos_de_5}")
