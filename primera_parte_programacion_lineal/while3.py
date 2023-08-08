'''desarrollar un programa que permita la carga de 10 valores por teclado (de uno en uno )
y nos muestre posteriormente la suma de los valores ingresados y su promedio '''


'''EN EL WHILE INDICA CUANDO TERMINA LA POSICION DE LA COLUMNA , EN ESTE CASO TERMINA EN x = x + 1, YA LUEGO
 PROMEDIO SE POSICIONA EN OTRA COLUMNA , OSEA EN LA PRIMERA Y AHI INDICA DONDE EMPIEZA Y TERMINA EL WHILE. '''

x = 1  # CONTADOR INICIADO EN 1
suma = 0 # VARIABLE SUMA DONDE SE VA A ALMACENAR LA SUMA

while x <= 10: #   ACA EMPIEZA EL WHILE
    numero = int(input("Ingrese numero :")) # SE INGRESA EL VALOR QUE QUEREMOS
    suma = suma + numero # ACA NUMERO INGRESADO SE VA ACUMULANDO EN LA VARIABLE SUMA HASTA QUE SE CUMPLA EL CICLO
    x = x + 1  #   ACA TERMINA EL WHILE
promedio = suma / 10
print(f"La suma de los valores es {suma}")
print(f"El promedio de los valores es {promedio}")
