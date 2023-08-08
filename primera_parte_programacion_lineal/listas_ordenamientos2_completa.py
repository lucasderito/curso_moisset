"""Se debe crear y cargar una lista donde almacenar 5 sueldos. ordenar de menor a mayor la lista
Ahora bien como vimos con el problema anterior con los 4 elementos que nos quedan podemos hacer el mismo
proceso visto anteriormente, con lo cual quedara ordenado otro elemento de la lista.
Este proceso lo repetiremos hasta que quede ordenada por completo la lista.
Como debemos repetir el algoritmo podemos englobar todo el bloque en otra estructura repetitiva
Realicemos una prueba del siguiente algoritmo:
1200
750
820
550
490
"""

lista_sueldos = []
for x in range(5):
    valor = int(input('Ingrese el sueldo :'))
    lista_sueldos.append(valor)
print(f'La lista original sin ordenar es :{lista_sueldos} ')
for k in range (4):# aca lo hacemos es un for que repita el for de adentro las veces necesarias para ordenar todo.
    for x in range (4):
        if lista_sueldos[x]> lista_sueldos[x+1]:
            aux = lista_sueldos[x]
            lista_sueldos[x] = lista_sueldos[x + 1]
            lista_sueldos[x + 1] = aux
print(f'La lista ordenada por completo es : {lista_sueldos}')



