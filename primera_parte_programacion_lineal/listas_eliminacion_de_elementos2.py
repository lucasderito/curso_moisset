"""Crear una lista y almacenar 10 elementos por teclado.
Eliminar todos los elementos que sean iguales al numero entero 5
"""

lista = []
for x in range(10):
    valor = int(input('Ingrese el valor :'))
    lista.append(valor)
print (f'Lista original : {lista}')
posicion = 0 # variable para moverse por la lista
while posicion < len(lista): # esto para hacer el mientras y recorrer la lista
    if lista[posicion] == 5 : # si la posicion de la lista osea el valor es = a 5
        lista.pop(posicion) # borramos el valor de esa misma posicion
    else: # sino hacemos posicion + 1 para pasar a comprobar el siguiente valor.
        posicion += 1
print (f'Listado con los valores eliminados segun consigna :{lista}')

