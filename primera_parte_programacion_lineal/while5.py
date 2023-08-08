'''realizar un programa que solicita ingresar 10 notas de alumnos y nos informe cuantos tienen notas
mayores o iguales a 7 y cuantos tienen notas menores'''

x = 1
mayores = 0
menores = 0

while x <= 10:
    nota = int(input("Ingrese la nota del alumno :"))
    if nota >= 7:
        mayores += 1
    else:
        menores += 1  # esto es lo mismo que hacer menores = menores + 1
    x +=1
print(f" La cantidad de alumnos con notas mayores o iguales a 7 es de : {mayores}")
print(f" La cantidad de alumnos con notas menores a 7 es de : {menores}")
