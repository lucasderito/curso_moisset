"""Se tiene la siguiente lista
lista=[[4, 12, 5, 66], [14, 6, 25], [3, 4, 5, 67, 89, 23, 1], [78, 56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 10 contenidos en todos
los elementos de la variable lista
volver a imprimir la lista
"""
lista=[[4, 12, 5, 66], [14, 6, 25], [3, 4, 5, 67, 89, 23, 1], [78, 56]]
print(f'La lista original es : {lista}')
for k in range(len(lista)):  # aca recorre todas los elementos que estan dentro de la lista y lo anida
    for x in range(len(lista[k])):  # recorro el contenido de la lista , osea las sublistas o listas dentro de ella
        if lista[k][x] > 10:
            lista[k][x] = 0
print(f'La lista modificada segun enunciado es :{lista}')


