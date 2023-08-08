""" es una actividad muy comun tener que buscar el mayor o el menor elemento de una lista
es necesario que las listas sean del mismo tipo de elementos, pueden ser enteros , o de caracteres y se busque
 cual es el mayor o menor alfabeticamente, pero no podemos buscar el mayor o el menor si la lista tiene
 cadenas de caracteres y enteros al mismo tiempo """
"""Problema de ejemplo 
Crear y cargar una lista con 5 enteros, implementar un algoritmo que identique el mayor valor de la lista"""

lista_enteros = []
for f in range(5):
    valor = int(input('Ingrese valor :'))
    lista_enteros.append(valor)
mayor = lista_enteros[0]  # aca creo una variable auxiliar que se llama mayor y le asigno el primer elemento de la lista
for x in range (1, 5): # aca lo que hago analizo la lista desde la posicion 1 a la 5,
    if lista_enteros[x]  > mayor: # aca comparo  el valor x si es mayor a la variable mayor que cree auxilarmente
        mayor = lista_enteros [x] # si es mayor mayor pasa a tomar el valor ingresado.
print ('Listado completo ingresado:')
print (lista_enteros)
print (f'El mayor valor de la lista es : {mayor}')