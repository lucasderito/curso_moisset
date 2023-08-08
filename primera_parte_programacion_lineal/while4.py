'''una planta que fabrica perfiles de hierro posee un lote de N piezas
confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese
la longitud de cada perfil , sabiendo que la pieza cuya longitud este comprendida en el rango de 1.20 y 1.30
son aptas, imprimir por pantalla la cantidad de piezas aptas que hay en el lote '''

x = 1
aptas = 0
n = int(input(" Ingrese la cantidad de piezas a procesar :"))
while x <= n:
    largo = float(input("Ingrese el largo de la pieza :"))
    if largo >= 1.20 and largo <= 1.30:
        aptas = aptas + 1
    x = x + 1
print(f"La cantidad de piezas aptas es :{aptas}")
