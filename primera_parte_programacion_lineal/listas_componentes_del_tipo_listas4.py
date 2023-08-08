"""Se tiene la siguiente lista :
lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]
Imprimir la lista , Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de lista
Volver a imprimir la lista"""

lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]
print (f"La lista original es : {lista}")
suma1 = 0  # aca inicializamos el contador para la primer suma.
for x in range(len(lista[0])):  # aca vamos a recorrer la lista [0] , osea [100, 7, 85, 8]
    if lista[0][x] > 50:  # aca la x va a recorrer cada uno de los elementos de la lista [0]
        lista[0][x]= 0
print(f'La lista modificada segun consigna es :{lista}')