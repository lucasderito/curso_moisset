"""Cuando se tienen listas paralelas y se ordenan los elementos de una de ellas, hay que tener
la precaucion de intercambiar los elementos de las listas paralelas"""

"""Problema : confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas.
Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los alumnos

Debe quedar claro que cuando intercambiamos las notas para dejarlas ordenadas de mayor a menor
debemos intercambiar los nombres para que las listas continueen paralelas.
Es decir que en los mismos subindices de cada lista continue la informacion relacionada"""

lista_alumnos = []
lista_notas =[]
for x in range (5):
    nombre = input('Ingrese el nombre del alumno :')
    lista_alumnos.append(nombre)
    nota = int(input('Ingrese la nota del alumno :'))
    lista_notas.append(nota)
print(f'Lista de alumnos {lista_alumnos}')
print(f'Las notas de los alumnos son :{lista_notas}')
for f in range (4):
    for x in range (4 - f):#recordemos que el menos f es para relacionar con el for de arriba para que no compare mal
        if lista_notas [x] < lista_notas [x + 1]:
            aux1 = lista_notas[x] # aux 1 para guardar la nota
            lista_notas[x] = lista_notas [x + 1]
            lista_notas [x + 1] = aux1
            aux2 = lista_alumnos [x] #aux 2 es para guardar el nombre del alumno e intercambiarlo tambien junto con aux1
            lista_alumnos[x] = lista_alumnos[x + 1]
            lista_alumnos [ x + 1] = aux2
"""vamos a hacer un print con un for para que imprima los valores concatenados"""
print("Lista de alumnos ordenados de mayor a menor ,con sus respectivas notas :")
for p in range (5): # este for p lo pongo p de print para guiarme yo , y para hacer el repetitivo de la impresion
    print(lista_alumnos[p] , lista_notas [p])# aca va a recorrer toda la lista e imprimiento los dos valores que pasamos