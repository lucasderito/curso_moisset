"""Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que crearemos en una lista.
El segundo valor indica la cantidad de elementos que tendra cada una de las listas internas de la lista principal.
Mostrar la lista y la suma de todos sus elementos.
Por ejemplo : Sin ingresamos por teclado un 2 y un 4, significa que debemos crear una lista similar a :
 lista =[[1, 1, 1, 1, ], [1, 1, 1, 1, ]]
 """
lista_principal = []
sublistas_de_lista_principal = int(input('Cuantas sublistas tendra su lista ? :'))
elementos_de_las_sublistas = int(input('Cuantos elementos tendra cada una de las sublistas ? :'))
for k in range (sublistas_de_lista_principal):
    lista_principal.append([]) # aca agrego la lista vacia a la lista principal, HASTA ACA AGREGO LA SUBLISTAS VACIAS.
    for x in range (elementos_de_las_sublistas):# A PARTIR DE ACA AGREGO LOS ELEMENTOS DE CADA SUBLISTA
        valor = int (input('Ingrese el valor :'))
        lista_principal[k].append(valor) # ACA ESTOY AGREGANDO UN VALOR A LA LISTA VACIA EN LA POSICION K
print(lista_principal)
# AHORA HACEMOS LA SUMA DE TODOS SUS ELEMENTOS.
suma = 0
for k in range (len(lista_principal)): # aca recorremos la lista principal
    for x in range(len(lista_principal [k] )):# aca recorremos cada una de las sublistas.. ose el k de la lista principal
        suma = suma + lista_principal [k] [x] # aca estoy sumando todos los elementos [x] de todas las sublistas [k]
print(f'La suma de todos los elementos de las sublistas contenidas en la lista principal es :{suma}')#
