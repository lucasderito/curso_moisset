'''Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde
a NAVIDAD'''

dia = int(input("Ingrese dia :"))
mes = int(input("Ingrese mes :"))
anio = int(input("Ingrese el anio :"))
if dia == 24 and mes == 12:
    print("La fecha ingresada ES NAVIDAD")
else:
    print("La fecha ingresada NO corresponde a NAVIDAD")
