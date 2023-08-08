"""Crer y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra.
Definir dos listas paralelas. Mostrar cuantos productos tiene un precio mayor al primer producto ingresado"""

lista_productos = []
precios_productos = []
for x in range(5):
    nombre_producto = input('Ingrese el nombre del producto :')
    lista_productos.append(nombre_producto)
    precio = int(input(' Ingrese el precio del producto :'))
    precios_productos.append(precio)
cantidad = 0
for x in range(1, 5):
    if precios_productos[x] > precios_productos [0]:
        cantidad += 1


print(f'La lista de productos es :{lista_productos}')
print(f'La lista de precio de los productos es :{precios_productos}')
print (f'La cantidad de productos con un precio mayor al primer producto ingresado es : {cantidad}')
