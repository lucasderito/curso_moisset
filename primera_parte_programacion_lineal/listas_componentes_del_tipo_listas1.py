"""hasta ahora hemos trabajado con listas cuyos componentes son de tipo , entero , flotantes, cadenas de caracteres
pero lo que hace tan flexible a esta estructura es que podemos almacenar en una lista componentes de TIPO LISTA
es decir una lista dentro de otra lista.. o varias listas dentro de una lista..
ejemplo :
notas [[4, 5], [8, 9], [10,5]]
aca estamos definiendo una lista de tres elementos del TIPO LISTA , osea en vez de ser una lista de enteros
flotantes o caracteres es una lista que contiene otras listas en su interior
en este caso es una lista que contiene tres listas de dos elementos cada lista """

"""problema:
-crear una lista por asignacion , la lista tiene que tener cuatro elementos
-cada elemento debe ser una lista de tres enteros 
-imprimir sus elementos accediendo de diferentes modos """
# aca tenemos una lista que contiene cuatro lista de tres enteros c/u
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(lista) #aca imprimimos la lista completa
print(lista[0])# aca imprimimos el primer componente
print(lista[1])# aca imprimimos el segundo componente
print(lista[2])# aca imprimimos el tercer componente
print(lista[3])# aca imprimimos el cuarto componente
print(lista [0][0])# aca estoy imprimiendo el primer componente de la primer lista de la lista.( el n 1 )
print(lista [0][1])# aca estoy imprimiendo el segundo componente de la primer lista de la lista ( el n 2)
# asi sucecesivamente con todos ..... otro ejemplo
print(lista [3][0])# aca deberia mostrarnos el n 10 .. ya que es el primer componente de la cuarta lista de la lista
"""-------------"""
print('Recorremos la primer lista de la lista:')
for x in range (len(lista[0])): # aca hacemos un for para imprimir TODA LA LISTA que corresponde a la primer lista.( 1 , 2, 3 )
    print(lista[0][x])# el [0] hace referencia a la primer lista, y el x es del for para recorrerla toda.
"""-------------"""
print('Imprimimos y recorremos todos los elementos de todas las listas.. mediante un for anidado:')
for f in range(len(lista)): # aca vamos a obtener la cantidad de listas de la lista ( osea las 4 listas)
    for x in range (len(lista[f])): # aca vamos a recorrer todos los elementos del subinidice f que viene del for de arriba
        print(lista[f][x])# aca imprimimos la lista con subindice f para el len de la lista y subinidice x para los elementos de las mismas



