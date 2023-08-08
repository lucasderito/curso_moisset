'''En una empresa trabajan N empleados cuyos sueldos oscilan entre $100 y $500 , realizar un programa
que lea los sueldos que cobra cada empleado e informar cuantos empleados cobran entre $100 y $300.Y cuantos cobran
mas de $300.
Ademas el programa debera informar el importe que gasta la empresa en sueldo de personal'''

x = 1
gasto_empresa = 0
sueldos_a_informar = 0
sueldos_a_informar_mas_300 = 0

n = int(input("Ingrese la cantidad de empleados a verificar sus sueldos :"))
while x <= n:
    sueldo = int(input("Ingrese el sueldo entre $100 y $500 : "))
    if sueldo >= 100 and sueldo <= 300:
        sueldos_a_informar += 1
    else:
        sueldos_a_informar_mas_300 +=1
    gasto_empresa = gasto_empresa + sueldo
    x += 1
print("La cantidad de sueldos entre $100 y $300 es de :", sueldos_a_informar)
print("La cantidad de sueldos de mas de $300 es de :", sueldos_a_informar_mas_300)
print("El gasto de la empresa en sueldos es de :", gasto_empresa)
