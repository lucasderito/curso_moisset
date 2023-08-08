"""En un curso de 4 alumnos se registraron las notas de sus examenes y se deben procesar de acuerdo a lo siguiente:
a - ingresar nombre y nota de cada alumno , se deben guardar en dos listas separadas.
b - realizar un listado que muestre los nombres , notas  y condicion del alumno. En la condicion colocar
'muy bueno ' si la nota es mayor o igual a 8 , 'bueno' si la nota esta entre 4 y 7 , y colocar 'insuficiente',
si la nota es inferior a 4.
c- imprimir cuantos alumnos tienen la leyenda muy bueno
"""

lista_alumnos = []
lista_notas_alumnos = []
for x in range(4):
    nombre = input(' Ingrese el nombre del alumno :')
    lista_alumnos.append(nombre)
    nota = int(input(' Ingrese la nota del alumno :'))
    lista_notas_alumnos.append(nota)

muy_bueno = 0
for x in range(4):
    print(lista_alumnos[x]) # al poner el print aca me lo va a mostrar intercalado cada nombre impreso
    print(lista_notas_alumnos[x])
    if lista_notas_alumnos[x] >= 8:
        print("Muy Bueno")
        muy_bueno += 1
    elif lista_notas_alumnos[x] >= 4 and lista_notas_alumnos[x] <= 7:
        print(" Bueno ")
    else :
        print("Insuficiente")
print(f'La cantidad de alumnos con calificacion muy buena es : {muy_bueno}')
