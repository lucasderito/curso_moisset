""""definir por asignacion una lista con 8 elementos enteros, contar cuantos de dichos valores
almacenan un valor superior a 100 """

lista = [10, 200, 300, 500, 200, 66, 67, 123]
contador = 0
x = 0
while x <len(lista):
    if lista[x] >100 :
        contador +=1
    x += 1
print(f"La cantidad de elementos de la lista superior a 100 es de : {contador}")
