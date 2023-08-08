'''Realizar un programa que permita cargar dos listas de 10 valores cada una.
informar con un mensaje cual de las 2 listas tiene un valor acumulado mayor
(mensaje lista 1 mayor , mensaje lista 2 mayor , listas iguales)
Tener en cuenta que puede haber dos o mas estructuras repetitivas en un algoritmo'''

lista1 = 0
lista2 = 0
x = 1
while x <= 10:
    valor = int(input("Ingrese valor de la lista 1: "))
    lista1 = lista1 + valor
    x += 1
x = 1
while x<= 10:
    valor = int(input("Ingrese valor de la lista 2  : "))
    lista2 = lista2 + valor
    x += 1

if lista1 > lista2:
    print("La lista 1 tiene un valor acumulado0 mayor")
elif lista1 < lista2:
    print(" La lista 2 tiene un valor acumulado mayor")
else:
    print("Las listas tienen el mismo valor acumulado")
