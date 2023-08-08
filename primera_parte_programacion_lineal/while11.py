'''Desarrollar un programa que nos permita cargar N numeros enteros y luego nos informe
cuantos valores fueron pares y cuantos valores fueron impares
Emplear el operador %  en la condicion de estructura condicional , este operador retorna el resto
de la division de dos valores, por ejemplo 11 % 2 retorna un 1 '''

x = 1
pares = 0
impares = 0

n = int(input("Ingrese la cantidad de valores que quiere ingresar por teclado :"))
while x <= n:
    valor = int(input("Ingrese el valor : "))
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1
    x +=1
print("La cantidad de numeros pares es de :",pares)
print("La cantidad de numeros impares es de :",impares)


