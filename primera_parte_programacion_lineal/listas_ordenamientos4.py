"""Solicitar por teclado la cantidad de empleados que tiene la empresa.
Crear y cargar una lista con todos los sueldos de dichos empleados.
 Imprimir la lista de sueldos ordenados de menor a mayor"""

lista_sueldos = []
cantidad_empleados = int(input('Ingrese la cantida de empleados :'))
for x in range(cantidad_empleados):
    sueldo = int(input('Ingrese el sueldo del empleado :'))
    lista_sueldos.append(sueldo)
print(f'Los sueldos de los empleados sin ordenar son : {lista_sueldos}')
for f in range(cantidad_empleados - 1):
    for x in range(cantidad_empleados - 1 - f):  # el - f viene del for f y es para que sea mas eficiente, que no haga comparaciones raras
        if lista_sueldos[x] > lista_sueldos[x + 1]:
            aux = lista_sueldos[x]
            lista_sueldos[x] = lista_sueldos[x + 1]
            lista_sueldos[x + 1] = aux
print(f'El listado de los sueldos ordenados es : {lista_sueldos}')
