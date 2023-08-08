'''confeccionar un programa que nos permita ingresar un valor del 1 al 10 y nos muestre la tabla
de multiplicar del mismo ( los primeros 12 terminos )
ejemplo : si ingreso 3 debera aparecer en pantalla los valores , 3 , 6, 9 , hasta el 36 '''

numero_elegido = int(input("Ingrese el numero que quiere saber su tabla de multiplicar entre 1 y 10 :"))
for tabla in range(1,13):
    print(tabla * numero_elegido)

