"""Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float )
obtener el promedio de las mismas, contar cuantas personas son mas altas que el promedio
y cuantas mas bajas """

lista = []
suma_alturas = 0
contador_mas_altas = 0
contador_mas_bajas = 0
for x in range(5):
    alturas = float(input("Ingrese la altura de la persona : "))
    lista.append(alturas)
    suma_alturas = suma_alturas + alturas
    promedio = suma_alturas / 5
for x in range(5):
    if lista[x] > promedio:
        contador_mas_altas += 1
    else:
        if lista[x] < promedio:
            contador_mas_bajas += 1

print(f"los elementos de la lista son : {lista}")
print(f"El promedio de alturas es : {promedio}")
print(f"Las cantidad de alturas mas bajas que el promedio son {contador_mas_bajas}")
print(f"Las cantidad de alturas mas altas que el promedio son {contador_mas_altas}")



""" tambien se puede resolver asi :
lista = []
suma_alturas = 0
contador_mas_altas = 0
contador_mas_bajas = 0

for x in range(5):
    altura = float(input("Ingrese la altura de la persona: "))
    lista.append(altura)
    suma_alturas += altura

promedio = suma_alturas / 5

for altura in lista:
    if altura > promedio:
        contador_mas_altas += 1
    elif altura < promedio:
        contador_mas_bajas += 1

print(f"Los elementos de la lista son: {lista}")
print(f"El promedio de alturas es: {promedio}")
print(f"La cantidad de alturas más bajas que el promedio es: {contador_mas_bajas}")
print(f"La cantidad de alturas más altas que el promedio es: {contador_mas_altas}")




"""