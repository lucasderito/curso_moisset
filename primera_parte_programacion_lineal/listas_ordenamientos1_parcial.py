""" LISTAS ORDENAMIENTO """
"""Otro algoritmo muy comun que debe conocer y entender un programador es el ordenamiento de una lista 
de datos. el ordenamiento de una lista se logra intercambiando los componentes de manera que :
lista [0] <= lista [1] <= lista [2].
El contenido del componente lista [0] sea menor o igual al contenido del componente lista [1] y asi 
sucesivamente. 
Si se cumple lo dicho anteriormente decimos que la lista esta ordenada de menor a mayor.
Igualmente podemos ordenar una lista de mayor a menor.
Tengamos en cuenta que la estructura de datos LISTA en python es mutable, eso significa que podemos modificar
sus elementos por otros.
Se puede ordenar tanto lista con componentes de tipo int , float , como cadena de caracteres STR .
En este ultimo caso el ordenamiento es alfabetico."""

""" Problema :
Se debe crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor mayor de la lista a la ultima 
posicion. 
la primera aproximacion para llegar en el proximo problema al ordenamiento completo de una lista tiene por objetivo 
analizar los intercambios de elementos dentro de una lista y dejar el mayor en la ultima posicion.
El algoritmo consiste en comparar si el primer componente es mayor a la segunda , en caso que la condicion sea
verdadera, intercambiamos los contenidos de los componentes.
Vamos a suponer que se ingresan los siguientes valores por teclado:
1200
750
820
550
490
"""

""" SOLO VAMOS A PONER EL ELEMENTO MAS GRANDE EN LA ULTIMA POSICION"""

lista_sueldos = []
for x in range(5):
    sueldo = int(input('Ingrese el sueldo :'))
    lista_sueldos.append(sueldo)
print(f'Lista original de sueldos : {lista_sueldos}')

# hasta aca se carga una lista como cualquier otra
"""====================================================="""
# ahora vamos a COMPARAR LOS ELEMENTOS
"""para comparar se utiliza un a posicion menos porque si comparamos el primer elemento con"
el segundo ya estamos utilizando un valor menos, osea que si tuviesemos 3 elementos tendriamos 
SOLO DOS COMPARACIONES y por eso eso que el for es un valor menos que la lista 
osea que : LAS CANTIDAD DE COMPARACIONES ES IGUAL AL LARGO DE LA LISTA - 1 """

for x in range(4):
    if lista_sueldos[x] > lista_sueldos[x + 1]:  # aca estamos comparando el primer elemento con el segundo.
        aux = lista_sueldos[x]  # aca guardo el valor si encuentra que es mayor , una variable auxiliar
        lista_sueldos[x] = lista_sueldos[x + 1] #aca realizo el intercambio le paso a la posicion x lo que hay en  la posicion x + 1
        lista_sueldos[x + 1] = aux #y aca en la posicion x + 1 se lo paso a la variable auxiliar.( INTERCAMBIO)
print(f'La lista con el mayor elemento al final de la misma quedaria: {lista_sueldos}')