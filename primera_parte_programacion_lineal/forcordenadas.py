'''escribir un programa que pida ingresar la coordenada de un punto en el plano , es decir dos valores enteros
distintos a cero , seria x e y . informar cuantos puntos se han ingresado en el primer , segundo , tercer y cuarto
parante, Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
parante 1 seria cuando x>0 e y>0
parante 2 seria cuando x<0 e y>0
parante 3 seria cuando x<0 e y<0
parante 4 seria cuando x>0 e y<0'''

parante1 = 0
parante2 = 0
parante3 = 0
parante4 = 0
eje = 0

n = int(input("Ingrese la cantidad de coordenadas a procesar :"))
for f in range(n):
    x = int(input("Ingrese el valor de X :"))
    y = int(input("Ingrese el valor de Y :"))
    if x > 0 and y > 0:
        parante1 += 1
    elif x < 0 and y > 0:
         parante2 += 1
    elif x < 0 and y < 0:
        parante3 += 1
    elif x > 0 and y < 0:
        parante4 += 1
    else:
        eje += 1
print(f"La cantidad de coordenadas en el primer parante es de {parante1}")
print(f"La cantidad de coordenadas en el segundo parante es de {parante2}")
print(f"La cantidad de coordenadas en el tercer parante es de {parante3}")
print(f"La cantidad de coordenadas en el cuarto parante es de {parante4}")
print(f"La cantidad de coordenadas sobre el eje es de :{parante1}")