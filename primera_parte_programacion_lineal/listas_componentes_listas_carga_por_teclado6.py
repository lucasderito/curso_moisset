"""Definir una lista y almacenar los nombres de 3 empleados.
 Por otro lado definir otra lista y almacenar en cada elemento una sublista con los numeros de dias del mes que el empleado falto.
 Imprimir los nombres de empleados y los dias que falto.
 Mostrar los empleados con la cantidad de inasistencias.
 Finalmente mostrar el nombre o los nombres de los empleados que faltaron menos dias."""


lista_empleados = []
lista_inasistencias =[]

for k in range (3):#este for principal es para agregar todo
    nombre = input('Ingrese el nombre del empleado :')# aca el nombre del empleado como siempre
    lista_empleados.append(nombre)# lo agregamos a la lista
    cant_faltas = int (input('Cuantos dias falto el empleado ? :'))# aca tenemos que preguntar cuantos dias falto
    lista_inasistencias.append([])# aca creamos las sublistas vacias dentro de lista_inasistencia
    for x in range (cant_faltas):# hacemos este for para poder ingresar los datos a las sublistas de lista_inasistencia
        dia_que_falto = int(input('Ingrese el dia que falto:'))# aca preguntamos los dias ( osea que fecha ) falto
        lista_inasistencias[k].append(dia_que_falto)# ACA IMPORTANTE , agregamos a lista inasistencias subindice K que viene del primer for
                                                    #mediante el metodo append y le pasamos el dia que falto con la variable dia_que_falto.

print('-------------------------------------------')
print('')

print('Nombre de empleado y dias que falto :')
for x in range (3):# con este for vamos a impirmir los dias del mes en los que falto cada empleado
    print('nombre empleado :',lista_empleados[x])#imprimimos el nombre del empleado de la lista_empleado la posicion x del for
    for f in range (len(lista_inasistencias[x])):#hacemos un for interno para recorrer la lista inasistencias con el LEN
       print('Las fechas del mes que falto fueron :', lista_inasistencias[x][f])# aca recorremos la lista inasistencia y la vamos asignando a cada empleado

print('-------------------------------------------')
print('')
print('Nombre de empleado y candidad de inasistencias que tuvo :')
for x in range (3):#este for es para imprimir la cantidad de faltas que tuvo el empleado
    print(f'nombre de empleado: {lista_empleados[x]}, tuvo: {len(lista_inasistencias[x])} faltas')
# en este ultimo print solo imprimimos mediante el for la lista empleados en su posicion [x] para que la recorra toda
# y la concatenamos con la lista de inasistencias tambien en su posicion [x] para que vaya recorriendo las listas paralelas

print('-------------------------------------------')
print('')
menor = len(lista_inasistencias[0]) # aca creamos una variable para saber cual es el menor valor de la lista inasistencias.
for x in range (1, 3):# recorremos de la posicion 1 a la 3 osea que es toda la lista
    if len(lista_inasistencias[x]) < menor:# preguntamos si en el largo LEN de la lista_inasistencias posicion [x] es menor que la variable MENOR que creamos
        menor = len(lista_inasistencias[x]) # si es asi , la variable menor va a tomar ese valor porque justamente es el menor y se guardara en lista_inasistencias[x]
print('Nombre/s del/los empleado/s que menos falto:')
for x in range (3): # ahora tenemos que hacer un for para ver cual es el empleado que tuvo menos faltas
    if len(lista_inasistencias[x]) == menor :# preguntamos si en el largo de la lista de inasistencias es igual al valor menor que sacamos antes
        print(lista_empleados[x])# imprimimos el empleado que menos falta tiene
