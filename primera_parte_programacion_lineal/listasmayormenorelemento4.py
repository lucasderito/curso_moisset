"""Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista.
Es decir si dicho valor se encuentra en 2 o mas posiciones de la lista"""

lista = []
for f in range(5):
    valor = int(input('Ingrese un valor entero :'))
    lista.append(valor)
mayor = lista[0]
cantidad = 0
for x in range(1, 5):
    if lista[x] > mayor:
        mayor = lista[x]
    if lista[x] == mayor :
        cantidad += 1

print(f"La lista completa de valores es :{lista}")
print(f'El numero de mayor valor es :{mayor}')
cantidad = 0
for x in range(5):
    if lista[x] == mayor :
        cantidad += 1
if cantidad > 1 :
    print(f'El valor mayor ({mayor}) se encuentra repetido')


""" MI SOLUCION ES DIFERENTE A LA DEL PROFESOR 

lista = []
for f in range(5):
    valor = int(input('Ingrese un valor entero :'))
    lista.append(valor)
mayor = lista[0]
cantidad = 0
for x in range(1, 5):
    if lista[x] > mayor:
        mayor = lista[x]
    if lista[x] == mayor :
        cantidad += 1
print(f"La lista completa de valores es :{lista}")
print(f'El numero de mayor valor es :{mayor}')
if cantidad > 1 :
    print(f'El valor mayor ({mayor}) se encuentra repetido')
    
    """
