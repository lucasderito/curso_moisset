"""Otra caracteristica fundamental de las listas en python, es que podemos eliminar cualquiera de sus
componentes, llamando al metodo pop e indicando la posicion del elemento a borrar

ejemplo :
Si tenemos la lista:

lista = [10, 20, 30 , 40 , 120]
y llamamos al metodo pop y le asignamos posicion (0)

lista.pop(0)

la lista nos quedaria asi :

lista = [20, 30 , 40 , 120]

otra cosa a resaltar es que cuando se elimina un elemento de la lista , este espacio no queda vacio
sino que la lista se acomoda. Los elementos siguientes al elemento eliminado
tomaran la posicion que tenian -1 posicion.Por lo tanto si un elemento tenia la posicion (5)
ahora tendra la posicion (4).

El metodo pop retorna el valor almacenado en la lista en la posicion indicada aparte de borrarlo

lista = [10, 20, 30 , 40]
print ( lista.pop(0))  ESTO NOS IMPRIMIRIA UN 10 .

"""
"""Problema : 
Crear una lista por asignacion con 5 enteros.Eliminar el primero el tercero y el ultimo de la lista """

lista = [10, 20, 30, 40, 50]
print(f'Lista original {lista}')
lista.pop(0) # aca eliminamos el primer elemento , recordemos que la posicion (0) es el primero.
print(lista) # aca se puede ir viendo
lista.pop(1) # aca al correrse la lista el tercer elementos que era la posicion(2) pasa a moverse a la (1)
print(lista)# aca se va viendo como se eliminan los elementos y se acomoda el resto, aca se ve el cambio de posicion
lista.pop(2)# y aca el mismo criterio al eliminarse dos elementos previamente la posicion (2)pasaria a ser la ultima
print(f'Lista con los elementos solicitados borrados {lista}')
