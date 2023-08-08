"""Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor
de la lista y la posicion donde se encuentra """

lista = []
for f in range(5):
    valor = int(input('Ingrese el valor :'))
    lista.append(valor)
aux_menor_valor = lista[0]
posicion = 0
for x in range(1, 5):
    if lista[x] < aux_menor_valor:
        aux_menor_valor = lista[x]
        posicion = x
print('La lista completa es :')
print(lista)
print('El menor valor es :')
print(aux_menor_valor)
print('La posicion donde se encuentra es :')
print(posicion) # recordar que la posicion empieza desde el 0