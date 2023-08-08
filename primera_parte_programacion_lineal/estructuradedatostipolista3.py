"""definir una lista por asignacion que almacene  en el primer componente el nombre de un alumno
y en las dos siguientes sus notas. Imprimer luego el nombre y el promedio de sus dos notas"""

lista_alumno = ['Lucas', 8, 9]
print(f"El nombre del alumno es :{lista_alumno[0]}") # aca imprimo el nombre del alumno
promedio = ((lista_alumno[1]) + (lista_alumno[2])) / 2 # aca saco el promedio de la suma de los dos elementos de la lista
print(f"El promedio del alumno es :{promedio}")
