"""Crear una lista por asignacion.
La lista tiene que tener dos elementos. Cada elemento tiene que ser una lista de 5 enteros.
Calcular y mostrar la suma de cada lista contenida en la lista principal"""
# estructura secuencial de suma , no se usa mucho
print('Esta es una manera de sumar los elementos de cada una de las listas que estan dentro de la lista contenedora')
print('')  # espacio en blanco
lista = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2]]
suma1 = lista[0][0] + lista[0][1] + lista[0][2] + lista[0][3] + lista[0][4]  # el [0]corresponde a la primer sublista
suma2 = lista[1][0] + lista[1][1] + lista[1][2] + lista[1][3] + lista[1][4]  # el [1]corresponde a la segunda sublista
print('La suma de los elementos de la primer sublista (elemento en realidad) es :')
print(suma1)
print('La suma de los elementos de la segunda sublista (elemento en realidad) es :')
print(suma2)
print('-------------------------------------------------')
print(' Ahora vamos a hacer la suma pero con un for ')  # el resultado sera igual que el primer ejemplo.
print('')  # espacio en blanco
suma1 = 0  # aca inicializamos el contador para la primer suma.
for x in range(len(lista[0])):  # aca vamos a recorrer la lista [0] , osea [1, 1, 1, 1, 1]
    suma1 = suma1 + lista[0][x]  # aca la x va a recorrer cada uno de los elementos de la lista [0]
suma2 = 0  # aca inicializamos el contador para la primer suma.
for x in range(len(lista[1])):  # aca vamos a recorrer la lista [1] , osea [2, 2, 2, 2, 2]
    suma2 = suma2 + lista[1][x]  # aca la x va a recorrer cada uno de los elementos de la lista [1]
print('La suma de los elementos de la primer sublista (elemento en realidad) es :')
print(suma1)
print('La suma de los elementos de la segunda sublista (elemento en realidad) es :')
print(suma2)
print('-------------------------------------------------')
print('Ahora vamos a hacer la suma con for anidados')
print('')
for k in range(len(lista)): # aca recorre todas los elementos que estan dentro de la lista y lo anida
    suma = 0 #inicializo contador
    for x in range(len(lista[k])):#recorro el contenido de la lista , osea las sublistas o listas dentro de ella
        suma = suma + lista[k][x]# y la [k] que recorreria la lista 0 y la lista 1 que estan dentro de la lista principal
    print(suma)                  # y la [x] seria para recorrer cada elemento o valor de las listas .. osea los [1] y los [2]
