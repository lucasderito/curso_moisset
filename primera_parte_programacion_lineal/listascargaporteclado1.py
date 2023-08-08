"""una lista en python es una estructura mutable , es decir que puede ir cambiando durante la ejecucion del
programa

ej .. definimos una lista
lista = [10,20,30]
print (len(lista))  nos mostraria 3 que es la cantidad de elementos que tiene la lista

ahora si usamos
lista.append (100)  esto nos agrega el valor 100 al final de la lista !!!!!!!!!METODO APPEND !!!!!!
si imprimimos con
print(len(lista)) ahora nos mostraria 4 que es la cantidad de elementos que tiene la lista
 si hacemos
 print (lista[0]) esto nos va a mostrar el numero 10 que es el primer valor de la lista
 print (lista[3]) esto nos va a mostrar el numero 100 que fue el elemento que agregamos y que se ubico en el
 subindice 3 """

""" EJERCICIO DE EJEMPLO 
definimos una lista vacia y solicitamos la carga de 5 enteros por teclado y aniadirlos a la lista
imprimir la lista generada """

lista = []
for x in range(5):
    valor = int(input("Ingrese un valor :"))
    lista.append(valor)  # append agrega valores a la lista
print("Los valores ingresados en la lista son :")
print(lista)
print("La cantidad de elementos de la lista es :")
print(len(lista))  # nos imprime la cantidad de elementos de la lista
