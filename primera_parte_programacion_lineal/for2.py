'''desarrollar un programa que permita la carga de 10 valores por teclado
y nos muestre posteriormente la suma de los valores ingresados y su promedio, este problema
ya lo resolvimos con while ahora lo vamos a hacer con el for'''

suma = 0
for x in range(10):
    valor = int(input("Ingrese el valor :"))
    suma = suma + valor
promedio = suma / 10
print(f"La suma de los valores es : {suma}")
print(f"el promedio de los valores es : {promedio}")
