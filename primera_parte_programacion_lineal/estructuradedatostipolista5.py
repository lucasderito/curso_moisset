"""definir una lista por asignacion con 5 enteros, mostrar por pantalla solo los elementos
con valor iguales o superior a 7"""
lista = [1, 3, 5, 7, 9]
x = 0
while x < len(lista):
    if lista[x] >= 7:
        print (lista[x])
    x += 1
