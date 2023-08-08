"""Realizar la carga de dos nombres de personas distintas.
Mostrar por pantalla luego ordenados alfabeticamente"""

nombre1 = input("Ingrese primer nombre :")
nombre2 = input("Ingrese segundo nombre :")
if nombre1 < nombre2:
    print("nombres ordenados alfabeticamente :")
    print(nombre1)
    print(nombre2)
else:
    print("nombres ordenados alfabeticamente :")
    print(nombre2)
    print(nombre1)
