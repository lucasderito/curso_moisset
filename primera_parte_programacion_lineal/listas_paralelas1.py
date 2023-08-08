"""podemos decir que dos listas son paralelas cuando hay una relacion entre los componentes de igual subindice
(misma posicion) de una lista y otra
"""

"""Ejercicio :
desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas.
luego de realizar la carga por teclado de todos los datos , imprimir los nombres de las personas mayores de edad
(mayores o iguales a 18 anios )"""

lista_nombres = []
lista_edades = []
for f in range(5):
    nombre = input('Ingrese el nombre de la persona :')
    lista_nombres.append(nombre)
    edad = int(input('Ingrese la edad de la persona :'))
    lista_edades.append(edad)
print('Listado de personas mayores de edad : ')
for x in range(5):
    if lista_edades[x] >= 18:
        print(f'{lista_nombres[x]} es mayor de edad.')
