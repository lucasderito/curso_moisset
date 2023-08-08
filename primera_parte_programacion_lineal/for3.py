'''escribir un programa que solicite por teclado 10 notas de alumnos
 y nos informe cuantos tienen notas mayores o iguales a 7 y cuantos menores'''

notas_mayores = 0
notas_menores = 0
for x in range(10):
    notas = int(input("Ingrese la nota de alumno :"))
    if notas >= 7:
        notas_mayores += 1
    else:
        notas_menores += 1
print(f"La cantidad de notas iguales o mayores a 7 es de : {notas_mayores}")
print(f"La cantidad de notas menores a 7 es de : {notas_menores}")
