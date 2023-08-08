""" Crear una lista por asignacion con la cantidad de elementos del tipo lista que usted desee.
Luego imprimir el ultimo elemento de la lista principal"""

lista = [['Marcos'], ['Juanjo', 'Susana', 'Juan Simon'], ['Luisina', 'Lucas', 'Bianca', 'Homero']]
print(len(lista))  # aca me va a devolver la cantidad de elementos ( osea sublistas en este caso hay 3 )
print(lista[len(lista) - 1]) # el largo de la lista -1 siempre va a ser el FINAL DE LA LISTA !!!!

"""LENG DE LISTA - 1 QUIERE DECIR QUE ES EL LARGO DE LA LISTA -1 LO QUE VA A UBICAR EL ULTIMO ELEMENTO
TAMBIEN PODEMOS HACER - 2 Y NOS VA A MOSTRAR EL ANTEULTIMO ELEMENTO """
print(lista[len(lista) - 2]) # ACA NOS MUESTRA EL ANTEULTIMO ELEMENTO