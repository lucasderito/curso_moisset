"""Desarrollar un programa que cree una lista de 50 elementos.
El primer elemento es una lista con  1 elemento, el segundo elemento es una lista con 2 elementos, y asi sucecivamente.
 """


lista = []
cantidad = 1 # creamos una variable que valga 1
for k in range(50): # hacemos el for de la cantidad de elementos (SUBLISTAS) que pide crear
    lista.append([])# agregamos la lista vacia para luego completar
    valor = 1 # hacemos una variable que sea 1
    for x in range(cantidad): # recorremos in range con el valor cantidad que era 1
        lista[k].append(valor) # y agregamos a cada una de las listas por eso el valor k agregamos la variable valor para que sume 1
        valor = valor + 1 # luego incrementamos valor en + 1
    cantidad += 1 # y a la cantidad tambien le agregamos 1 , FUERA DEL FOR  INTERNO.
print(lista)# aca nos va a imprimir de forma comun .. en una sola linea.
print('-------------------------------------------')
print('')
print(' Aca nos va a imprimir una debajo de la otra con un bucle for vamos a hacer que las imprima debajo :')
for x in lista:
    print(x)