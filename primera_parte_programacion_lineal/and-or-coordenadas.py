'''escribir un programa que pida ingresar la coordenada de un punto en el plano , es decir dos valores enteros
distintos a cero , seria x e y . posteriormente imprimir en pantalla en que parante se indica dicho punto, si algun
de los valores es CERO es porque se encuentra sobre un eje, informarlo
parante 1 seria cuando x>0 e y>0
parante 2 seria cuando x<0 e y>0
parante 3 seria cuando x<0 e y<0
parante 4 seria cuando x>0 e y<0'''

x = int(input("Ingrese el valor de X :"))
y = int(input("Ingrese el valor de Y :"))

if x > 0 and y > 0:
    print("el punto den el plano se encuentra en el PRIMER PARANTE")
elif x < 0 and y > 0:
    print("el punto den el plano se encuentra en el SEGUNDO PARANTE")
elif x < 0 and y < 0:
    print("el punto den el plano se encuentra en el TERCER PARANTE")
elif x>0 and y<0:
    print("el punto den el plano se encuentra en el CUARTO PARANTE")
else:
    print("el punto den el plano se encuentra SOBRE UN EJE")
