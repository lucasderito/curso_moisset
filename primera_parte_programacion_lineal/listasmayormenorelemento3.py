"""Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista
mostar el nombre de persona menor en orden alfabetico"""

lista_nombres = []
for f in range(5):
    nombres = (input('Ingrese el nombre de la persona :'))
    lista_nombres.append(nombres)
nombre_menor = lista_nombres[0]
for x in range(1, 5):
    if lista_nombres[x] < nombre_menor:
        nombre_menor = lista_nombres[x]
print(f'La lista completa de nombres es : {lista_nombres}')
print(f'La persona con el nombre de menor orden alfabetico es : {nombre_menor}')
