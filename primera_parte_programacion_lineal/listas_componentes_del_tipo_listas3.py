"""Crear una lista por asignacion.La lista tiene que tener 5 elementos.
Cada elemento debe ser una lista.
- la primer lista tiene que tener un elemento
- la segunda lista tiene que tener dos elementos
- la tercer lista tiene que tener tres elementos
-la cuarta lista tiene que tener cuatro elementos
-la quinta lista tiene que tener cinco elementos
Sumar todos los valores de las listas"""
lista = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
suma = 0  # inicializo contador
for k in range(len(lista)):  # aca recorre todas los elementos que estan dentro de la lista y lo anida
    for x in range(len(lista[k])):  # recorro el contenido de la lista , osea las sublistas o listas dentro de ella
        suma = suma + lista[k][x]  # y la [k] que recorreria la lista 0 y la lista 1 que estan dentro de la lista principal
print(suma)  # y la [x] seria para recorrer cada elemento o valor de las listas .. osea los [1] y los [2]
# DATALLE A TENER EN CUENTA .. EL PRINT VA FUERA DEL FOR PARA QUE ME IMPRIMA LA SUMA DE TODOS !! ..
 # SI QUISIERA QUE ME MUESTRE LA SUMA DE CADA UNO DE LAS LISTAS.. EL PRINT DEBERIA PONERLO ALINEADO DEBAJO DE SUMA, DENTRO DEL FOR