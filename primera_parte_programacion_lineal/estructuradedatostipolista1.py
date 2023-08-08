"""definir una lista  que almacene 5 enteros . Sumar todos sus elementos y mostrar dicha suma"""
lista=[10,20,30,40,50]
suma = 0
x = 0
while x <len(lista):
    suma = suma + lista[x]
    x += 1
print(f"Los elementos de la lista son : {lista}")
print(f"La suma de todos los elementos de la lista es : {suma}")