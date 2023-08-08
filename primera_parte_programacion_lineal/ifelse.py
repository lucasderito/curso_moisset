'''se ingresan tres notas de un alumno , si el promedio es mayor o igual a 7 mostrar un mensaje
que diga PROMOCIONADO'''

nota1 = int(input("Ingrese la primer nota :"))
nota2 = int(input("Ingrese la segunda  nota :"))
nota3 = int(input("Ingrese la tercer nota :"))

promedio = (nota1 + nota2 + nota3) / 3
if promedio > 7:
    print("El alumno esta promocionado")
else:
    print("El alumno no esta promocionado")
