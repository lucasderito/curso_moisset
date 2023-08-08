'''realizar un programa que solicite la carga de dos numeros por teclado
si el primero es mayor al segundo informar su suma y su diferencia
en caso contrario informar el producto y la division del primero con respecto al segundo'''

n1 = float (input("Ingrese el primer numero :"))
n2 = float (input("Ingrese el segundo numero :"))
if n1>n2:
    suma = (n1+n2)
    resta = (n1-n2)
    print ("la suma de los numeros es :")
    print  (suma)
    print ("la resta de los numeros es :")
    print  (resta)
    #print(f"el numero mayor es {n1}" )
else:

    producto = (n1*n2)
    division = (n1 / n2)
    print("el producto de los numeros es :")
    print (producto)
    print("la division de los numeros es :")
    print(division)
    #print (f"el numero mayor es {n2}" )