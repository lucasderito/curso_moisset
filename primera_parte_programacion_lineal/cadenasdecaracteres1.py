"""vamos con algunos ejemplos """

nombre = 'juan'
print (nombre[0]) # aca nos muestra la j porque el subindice 0 es la primer letra de juan , en este caso j
if nombre [0]== 'j': #aca estamos preguntando si empieza con j
    print(f"{nombre} empieza con j" )


""" ahora hagamos un ejercicio 
solicitar la carga del nombre de una persona en minuscula ,mostrar un mensaje si comienza con vocal dicho nombre"""

nombre = input("Ingrese un nombre en minuscula :")
if nombre[0] == 'a' or nombre[0] == 'e' or nombre[0] == 'i' or nombre[0] == 'o' or nombre[0] == 'u' :
    print (f" el nombre {nombre} comienza con una vocal")
else:
    print(f" el nombre {nombre} no comienza con una vocal")