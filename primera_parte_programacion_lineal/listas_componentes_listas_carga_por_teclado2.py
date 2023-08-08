"""Se tiene que cargar la siguiente informacion
-Nombres de 3 empleados
-Ingresos en concepto de sueldo cobrado por cada empleado en los ultimos 3 meses.
Confeccionar un programa para :
a) Realizar la carga de los nombres de los empleados y los 3 sueldos de cada empleado.
b)Generar una lista que contenga el ingreso acumulado en sueldos en los ultimos 3 meses para cada empleado.
c)Mostrar por pantalla el total pagado en sueldos a cada empleado en los ultimos 3 meses.
d)Obtener el nombre del empleado que obtuvo el mayor sueldo acumulado.

Es importante notar que estos datos no los cargaremos por asignacion sino que las cargaremos por teclado a las 2
primeras listas y la tercer lista la obtendremos extrayendo los datos de la lista sueldos.
"""

lista_empleados = []
lista_sueldos = []
sueldo_acumulados = []
for x in range(3):
    nombre = input('Ingrese el nombre del empleado :')
    lista_empleados.append(nombre)
    sueldo1 = int(input('Ingrese el primer sueldo :'))
    sueldo2 = int(input('Ingrese el segundo sueldo :'))
    sueldo3 = int(input('Ingrese el tercer sueldo :'))
    lista_sueldos.append([sueldo1, sueldo2, sueldo3])
for x in range(3):
    total_sueldos = lista_sueldos[x][0] + lista_sueldos[x][1] + lista_sueldos[x][2] # recorremos la lista y sumamos sus subindices
    sueldo_acumulados.append(total_sueldos)# agregamos a la lista sueldo acumulados la operacion de suma de arriba.
print('Empleados :')
print(lista_empleados)
print('Sueldos :')
print(lista_sueldos)
print('Sueldo acumulado de los empleados :')
print(sueldo_acumulados)
print('-----------------------')
print('')
"""------------------"""
# OTRA FORMA DE IMPRIMIR.
for f in range(3):
    print(f'Empleado : {lista_empleados[f]}, sueldos :{lista_sueldos[f][0]}, {lista_sueldos[f][1]}, {lista_sueldos[f][2]}, sueldo acumulado :{sueldo_acumulados[f]}')
# AHORA VAMOS A HACER EL ULTIMO PUNTO

posmayor = 0 # establezco un contador
mayor = sueldo_acumulados[0]# aca estoy diciendo que el primer elemento es el mayor para luego empezar a comprar con los otros mediante un for.
for x in range (1, 3): # partimos de 1 porque 0 ya pusimos arriba que es el mayor , hastas la posicion 3
    if sueldo_acumulados[x] > mayor: # aca recorremos y comparamos el valor si es mayor que sueldo acumulados [0]
        mayor = sueldo_acumulados[x] # aca guardamos mayor en sueldo_acumulados[x]
        posmayor = x # y aca decimos que posmayor ( la variable que inicializamos ) es igual a x , entonces x pasa a ser el mayor.
print(f'El empleado con mayor sueldo acumulado es : {lista_empleados[posmayor]} con un ingreso de : {mayor}')# concatenamos el nombre del empleado con la variable posmayor que obtuvimos recien