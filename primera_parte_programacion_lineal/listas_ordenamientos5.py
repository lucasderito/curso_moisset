"""Cargar una lista con 5 elementos enteros.Ordenarla de menor a mayor y mostrarla por pantalla
luego ordenar de mayor a menor e imprimir el resultado nuevamente"""

lista_enteros = []
for x in range(5):
    valor = int(input('Ingrese el valor :'))
    lista_enteros.append(valor)
print(f'La lista de enteros sin ordenar de ninguna forma es : {lista_enteros}')
for f in range(4):
    for x in range(4):
        if lista_enteros[x] > lista_enteros[x + 1]:
            aux = lista_enteros[x]
            lista_enteros[x] = lista_enteros[x + 1]
            lista_enteros[x + 1] = aux
print(f'La lista ordenada de menor a mayor es :{lista_enteros}')

""" ORDENADA DE MAYOR A MENOR """
for f in range(4):
    for x in range(4):
        if lista_enteros[x] < lista_enteros[x + 1]:
            aux = lista_enteros[x]
            lista_enteros[x] = lista_enteros[x + 1]
            lista_enteros[x + 1] = aux
print(f'La lista ordenada de mayor a menor es :{lista_enteros}')
