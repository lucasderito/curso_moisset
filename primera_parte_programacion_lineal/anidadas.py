'''hacer un programa que pida por teclado tres notas de un alumno , calcular el promedio y
si el promedio es mayor  o igual a 7 mostra un menesaje que diga PROMOCIONADO
si el promedio es mayor a 4 y menor a 7 el mensaje tiene que decir REGULAR
y si es menor a 4 mostrar por mensaje REPROBADO'''

nota1 = int(input("Ingrese la primer nota :"))
nota2 = int(input("Ingrese la segunda nota :"))
nota3 = int(input("Ingrese la tercer nota :"))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 7:
    print("El alumno esta PROMOCIONADO")
else:
    if promedio >= 4:
        print("El alumno esta REGULAR")
    else:
        print("El alumno esta REPROBADO")
