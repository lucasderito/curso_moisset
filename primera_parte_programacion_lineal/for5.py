'''confeccionar un programa que lea N numeros enteros y calcule la cantidad de valores mayores
 a 1000 ( n se carga por teclado ) .Lo primero que se hace es cargar una variable que indique la cantidad
de valores a ingresar , dicha variable se carga antes de entrar en la estructura repetitiva for '''

cantidad = 0
n = int (input(" Ingrese cuantos valores ingresara :"))
for f in range(n):
    valor =int(input("Ingrese el valor :"))
    if valor > 1000:
        cantidad += 1
print(f"La cantidad de numeros mayores a 1000 es de :{cantidad}")