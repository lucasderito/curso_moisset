'''Se realiza la carga de 10 valores enteros por teclado . Se desea conocer :
a)La cantidad de valores ingresados negativos
b)La cantidad e valores ingresados positivos
c)La cantidad de multiplos de 5
d)El valor acumulado de los numeros ingresados que son pares'''

positivos = 0
negativos = 0
multiplos5 = 0
valor_acumulado_pares = 0
for f in range(10):
    valor = int(input("Ingrese el valor :"))
    if valor > 0:
        positivos += 1
    if valor < 0:
        negativos += 1
    if valor % 5 == 0:
        multiplos5 += 1
    if valor % 2 == 0:
        valor_acumulado_pares = valor_acumulado_pares + valor
print(f"La cantidad de numeros ingresados positivos es :{positivos}")
print(f"La cantidad de numeros ingresados negativos es :{negativos}")
print(f"La cantidad de numeros multiplos de 5 es de : {multiplos5}")
print(f"La suma acumulada de numeros pares es de :{valor_acumulado_pares}")
