"""Definir 2 listas de 3 elementos ( osea 3 sublistas dentro de cada una de las listas.)
La primer lista esta constituida por una sublista con el nombre del padre y la madre de una familia.
La segunda lista esta constituida con los nombres de los hijos de cada familia. Puede haber familias sin hijos.
Imprimir los nombres del padre la madre y sus hijos.
Tambien imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.

Un ejemplo si se define por asignacion seria :

lista_padres = [["Juan", "Susana "], ["Chiche", "Chichita"], ["Lucas", "Luisina"]]
lista_hijos = [["Luisina", "Juan Simon"], [], ["Bianca", "Homero", "Hunty"]]

Como son dos listas paralelas podemos decir que la familia cuyos padres son Juan y Susana tiene dos hijos que son
Luisina y Juan Simon, la familia cuyos padres son Chiche y Chichita no tienen hijos, mientras que la familia cuyos
padres son Lucas y Luisina tienen por hijos a Bianca, Homero y Hunty.
"""

lista_padres = []
lista_hijos = []
for f in range (3):
    padre = input('Ingrese el nombre del padre :')
    madre = input('Ingrese el nombre de la madre :')
    lista_padres.append([padre , madre]) # aca agregamos tanto el padre como la madre, osea es una lista con 2 elementos.
    cant_hijos = int(input('Cuantos hijos tiene esta familia ?:')) # aca vamos a preguntar cuantos hijos vamos a ingresar.
    lista_hijos.append([])  # aca le pasamos una lista vacia para que cree la lista y asi poder ingresar los hijos
    for x in range (cant_hijos): # aca lo que vamos a hacer es un for por la cantidad de hijos que ingresamos por el input
        hijo = input('Ingrese el nombre del hijo :')
        lista_hijos[f].append(hijo)# aca usamos el [f] para la cantidad , viene del mismo FOR PRINCIPAL

print('Listado del padre, la madre y sus hijos :')
for k in range (3): # hacemos este for para imprimir las 3 familias.
    print('padre', lista_padres[k][0]) # aca vamos a imprimir los padres que estan en la posicion [k] del for subindice [o]
    print('madre', lista_padres [k][1]) # aca vamos a imprimir las madres que estan en la posicion [k] del for subinidice [1]
    for x in range(len(lista_hijos[k])):# aca hacemos un for para imprimir los hijos de cada una de las familias [k]
        print('hijo:',lista_hijos[k][x]) # aca hacemos un print de todos los hijos de la posicion [k] que seria la familia y la posicion [x] que seria cada uno de los hijos
print('Listado del PADRE y la cantidad de hijos que tiene :')
for x in range (3): # este for es para recorrer los padres ahora vamos a usar su posicion.
    print('padre', lista_padres[x][0])# aca elejimos que imprima solo el padre , la x es del for y la posicion [0] es del padre
    print('La cantidad de hijos que tiene :', len(lista_hijos[x]))



