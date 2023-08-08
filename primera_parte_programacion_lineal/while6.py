'''se ingresa un conjunto de N alturas de personas por teclado, mostrar la altura promedio de
las personas '''

x = 1
suma_alturas = 0

n = int(input(" Ingrese la cantidad de personas que quiere ingresar su altura :"))
while x <= n:
    altura = float(input("Ingrese la altura de la persona :"))
    suma_alturas += altura
    x += 1
promedio_alturas = suma_alturas / n
print("La altura promedio de las personas es :", promedio_alturas)
