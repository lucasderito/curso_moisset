'''de un operario se conoce su sueldo y los anios de antiguedad, se pide confeccionar un programa que lea
los datos de entrada e informe:

A- si el sueldo es inferior a 500 y su antiguedad es igual o superior a 10 anios, otorgarle un aumento del 20 %
e informar su sueldo a cobrar .
B-si el sueldo es inferior a 500 pero su antiguedad es menor a 10 anios , otorgarle un aumento del 5 % e informar
su sueldo a cobrar
C-si su sueldo es mayor o igual a 500 mostrar el sueldo en pantalla si cambios.
'''
sueldo = int(input("Ingrese el sueldo del operario :"))
antiguedad = int(input("Ingrese los anios de antiguedad del operario :"))

if sueldo < 500 and antiguedad >= 10:
    aumentodel10 = sueldo * 0.20
    sueldo_final = sueldo + aumentodel10
    print(f"El sueldo con su correspondiente aumento es :{sueldo_final}")
elif sueldo < 500 and antiguedad < 10:
    aumentodel5 = sueldo * 0.05
    sueldo_final = sueldo + aumentodel5
    print(f"El sueldo con su correspondiente aumento es :{sueldo_final}")
else:
    print(f"El sueldo del operario es {sueldo}")
