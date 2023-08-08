"""Crear dos listas paralelas.
En la primera ingresar los nombres de los empleados
En la segunda ingresar los sueldos de los empleados
Ingresar por teclado cuando se inicia el programa la cantidad de empleados de la empresa
Borrar luego todos los empleados que tienen un sueldo mayor a 10000
Tanto el sueldo como el nombre deberian eliminarse ya que se trata de listas paralelas."""

lista_empleados = []
lista_sueldos = []
cant_empleados = int(input('Ingrese la cantidad de empleados a procesar:')) # desde aca es la carga de siempre
for x in range(cant_empleados):
    nombre = input('Ingrese el nombre del empleado :')
    lista_empleados.append(nombre)
    sueldo = int(input('Ingrese el sueldo del empleado :'))
    lista_sueldos.append(sueldo)
print ('La Lista de los empleados original con sus sueldos :' ) # hacemos un for para imprimir las listas
for x in range (len(lista_empleados)):# aca se puede usar tanto la lista sueldo como la empleados pq son paralaleas
    print (lista_empleados[x], lista_sueldos[x])

posicion = 0 # aca hacemos una variable para recorrer todas las posiciones
while posicion<len(lista_sueldos):
    if lista_sueldos[posicion] > 10000:
        lista_sueldos.pop(posicion) # se eliminan ambas listas pq son paralelas
        lista_empleados.pop(posicion)# se eliminan ambas listas pq son paralelas
    else:
        posicion += 1
print ('La lista final con los elementos eliminados segun consigna ( que sean mayor a 10000 ) es :')
for x in range (len(lista_empleados)):# aca se puede usar tanto la lista sueldo como la empleados pq son paralaleas
    print (lista_empleados[x], lista_sueldos[x])