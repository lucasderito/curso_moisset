"""Almacenar en una lista los sueldos ( valores float ) de 5 operarios
Imprimir la lista y el promedio de sueldos """

lista = []
suma_sueldos = 0
for x in range(5):
    sueldo_empleado = float(input("Ingrese el sueldo del empleado :"))
    lista.append(sueldo_empleado)
    suma_sueldos = sueldo_empleado + suma_sueldos
    promedio_empleados = suma_sueldos / 5
print(f"Los sueldos ingresados a la lista son :{lista}")
print(f"El promedio de sueldos de los empleados es : {promedio_empleados} ")
