'''Realizar la carga de enteros por teclado ,  preguntar despues que ingresa el valor si
desea cargar otro valor debiendo el operador ingresar la cadena si o no por teclado
mostrar la suma de los valores ingresados '''

suma = 0
opcion = "si"
while opcion == "si":
    numero = int(input("Ingrese un valor entero :"))
    suma = suma + numero
    opcion = input("Desea cargar otro valor ? si/no : ")
print(f"La suma de los valores ingresados es {suma}")

""" siempre es aconsejable resolver con el while cuando existe una actividad repetitiva
que actue bajo una condicion """
