"""Realizar la carga de valores enteros por teclado y almacenarlos en una lista
finalizar la carga de enteros al ingresar el numero cero (0)
mostrar finalmente el tamano de la lista y el contenido de la lista """

lista = []
valor = int(input("Ingrese un valor entero ( si el valor ingresado es 0 el programa termina) :"))
while valor != 0 :
    lista.append(valor)
    valor = int(input("Ingrese un valor entero ( si el valor ingresado es 0 el programa termina) :"))
print("Los valores ingresados en la lista son :")
print(lista)
print("La cantidad de elementos de la lista es :")
print(len(lista))  # nos imprime la cantidad de elementos de la listaS
