'''confeccionar un programa que nos permita ingresar un numero positivo y nos muestre desde el 1
hasta ese valor ingresado de 1 en 1
ejemplo si ingresamos 30 nos debe mostrar del 1 al 30 '''

finlista = 1
numeroingresado = int(input("Ingrese el numero donde finalizara el conteo :"))
while finlista <= numeroingresado:
    print(finlista, end='-')
    finlista = finlista + 1
