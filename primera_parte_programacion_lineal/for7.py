'''desarrollar un programa que solicite la carga de 10 numeros e imprima la
suma de los ultimos 5 valores ingresados '''

suma = 0
for f in range (10):
    num = int (input("Ingrese el numero :"))
    if f >= 5:
        suma = suma + num
print (f"La suma de los ultimos 5 numeros ingresados es {suma}")