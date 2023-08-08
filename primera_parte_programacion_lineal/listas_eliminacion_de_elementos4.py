"""Crear una lista de 5 enteros y cargarlos por teclado.
Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores"""

lista1 = []
for x in range (5):
    valor = int(input('Ingrese el valor :'))
    lista1.append(valor)
print (f'Lista original : {lista1}')
# hasta aca creamos la lista como siempre

# ahora lo que vamos a hacer es recorrer la lista e ir eliminando lo que pide y pasandolo a una nueva lista
# para eso creamos una lista nueva vacia
lista2 = []
posicion = 0 # para recorre la lista como siempre
while posicion<len(lista1):
    if lista1[posicion] >= 10 : # preguntamos la condicion si se cumple .. vamos abajo y hacemos
       lista2.append(lista1.pop(posicion))# aca estamos agregando a la lista 2
                                          # lo que estamos sacando de la lista 1
    else:
        posicion += 1
print(f'La lista original luego de borrar lo que pide es : {lista1}')
print(f' La lista generada ( lista2 ) con los valores eliminados de la lista1 es : {lista2} ')
