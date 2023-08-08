"""Se necesita saber la temperatura media trimestral de 4 paises.
Para ello se tiene como dato 3 temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del pais y seguidamente las tres temperaturas medias mensuales
Seleccionar la estructura de datos adecuada para el almacenamiento de los datos en memoria
a)Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
b)Imprimir los nombres de los paises y las temperaturas medias mensuales de las mismas.
c)Calcular la temperatura media trimestral de cada pais.
d)Imprimir los nombres de los paises y las temperaturas medias trimestrales.
e)Imprimir el nombre del pais con la temperatura media trimestral mayor.
"""

lista_paises = []
lista_temperaturas_media = []
lista_promedio_temperaturas = []
for x in range (4):
    pais  = input('Ingrese el nombre del pais :')
    lista_paises.append(pais)
    temp1 = int(input('Ingrese la  primer temperatura media del pais:'))# aca cargamos la primer temperatura
    temp2 = int(input('Ingrese la  segunda temperatura media del pais:'))# aca cargamos la segunda temperatura
    temp3 = int(input('Ingrese la  tercer temperatura media del pais:'))# aca cargamos la tercer temperatura
    lista_temperaturas_media.append([temp1, temp2, temp3]) # aca agregamos las tres temperaturas a lista_temperatura_media
print('-------------- impresion de listas sin procesar------------------------------')
print(lista_paises)
print(lista_temperaturas_media)
print('---------------------------------------------------------------------------------------------')
print('')
print('Paises y sus temperaturas medias mensuales de los ultimos tres meses :')
for x in range(4):# aca hacemos un for para imprimir cada uno de los resultados , donde imprimimos paises y temperaturas
    print(lista_paises[x], lista_temperaturas_media[x] [0], lista_temperaturas_media[x] [1], lista_temperaturas_media[x][2])
for x in range (4):# ahora vamos a hacer un for para sacar los promedios.
    prom = (lista_temperaturas_media[x] [0] + lista_temperaturas_media[x] [1] + lista_temperaturas_media[x][2]) / 3
    lista_promedio_temperaturas.append(prom)# aca guardamos el promedio de las temperaturas en la lista promedio temperaturas
print('---------------------------------------------------------------------------------------------')
print('')
print('Listado de paises y temperaturas medias trimestrales :')
for x in range (4):# este for es para imprimir el listado de paises y sus temperaturas medias.
    print(lista_paises[x], lista_promedio_temperaturas[x]) # aca imprimimos de la lista las posiciones que queremos.
print('---------------------------------------------------------------------------------------------')
print('')
posmayor = 0 # variable para poder almacenar la posicion mayor una vez recorrida la lista
for x in range (1, 4):
    if lista_promedio_temperaturas[x] > lista_promedio_temperaturas [posmayor] : # aca comparamos el primer valor con la variable pos mayor que va recorriendo el for
        posmayor = x # aca posmayor tomaria el valor de X .. en el caso que sea mayor como la condicion de arriba asi lo indica
print(f'Pais con temperatura media trismestral mayor :{lista_paises[posmayor]}')# aca imprimimos de la lista paises la posicion mayor.



