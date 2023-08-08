"""Realizar un programa  que pida la carga de 2 listas numericas enteras de 4 elementos cada una
 Generar una tercer lista que surja de la suma de los elementos de la misma  posicion de cada lista
 mostrar esta tercer lista"""

lista1 = []
lista2 = []
lista_sumada = []
print(' Carga de la primer lista')
for x in range (4):
    valor_lista_1 = int(input('Ingrese valor para la primera lista :'))
    lista1.append(valor_lista_1)
print(' Carga de la segunda lista')
for x in range (4):
    valor_lista_2 = int(input('Ingrese valor para la segunda lista :'))
    lista2.append(valor_lista_2)
for x in range (4):
    suma = lista1[x] + lista2 [x]
    lista_sumada.append(suma)
print(f'Primer lista {lista1}')
print(f'Segunda lista {lista2}')
print(f'Listas sumadas : {lista_sumada}')
