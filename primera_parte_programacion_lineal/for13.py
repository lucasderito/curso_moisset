'''se cuenta con la siguiente informacion :
- las edades de 5 estudiantes del turno manana
- las edades de 6 estudiantes del turno tarde
- las edades de 8 estudiantes del turno noche
Las edades de cada estudiante deben ingresarse por teclado
a) obtener el promedio de las edades de cada turno ( tres promedios )
b)imprimir dicho promedio
c)mostar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor'''

suma_manana = 0
suma_tarde = 0
suma_noche = 0
for f in range(5):
    edad_manana = int(input(" Ingrese la edad del alumno turno manana :"))
    suma_manana = suma_manana + edad_manana
promedio_manana = suma_manana / 5
for f in range(6):
    edad_tarde = int(input(" Ingrese la edad del alumno turno tarde :"))
    suma_tarde = suma_tarde + edad_tarde
    promedio_tarde = suma_tarde / 6
for f in range(8):
    edad_noche = int(input(" Ingrese la edad del alumno turno noche :"))
    suma_noche = suma_noche + edad_noche
    promedio_noche = suma_noche / 8
if promedio_manana > promedio_tarde and promedio_manana > promedio_noche:
    print(f"El turno con mayor promedio de edad es el turno manana")
elif promedio_tarde > promedio_manana and promedio_tarde > promedio_noche:
    print(f"El turno con mayor promedio de edad es el turno tarde")
else:
    print(f"El turno con mayor promedio de edad es el turno noche")

print(f"El promedio del turno manana es {promedio_manana}")
print(f"El promedio del turno tarde es {promedio_tarde}")
print(f"El promedio del turno tarde es {promedio_noche}")