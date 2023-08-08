"""Una empresa tiene dos turnos ( manana y tarde )  en la que trabajan 8 empleados
(4 por la manana y 4 por la tarde ).
confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en 2 lista
Imprimir las dos listas de sueldos"""

lista_sueldos_manana = []
print ('Sueldos del turno manana')
for f in range (4):
    valor = float (input('Ingrese sueldos manana :'))
    lista_sueldos_manana.append(valor)
lista_sueldos_tarde = []
print ('Sueldos del turno tarde')
for f in range (4):
    valor = float (input('Ingrese sueldos tarde :'))
    lista_sueldos_tarde.append((valor))
print (f'La lista de sueldos del turno manana es {lista_sueldos_manana}')
print (f'La lista de sueldos del turno manana es {lista_sueldos_tarde}')