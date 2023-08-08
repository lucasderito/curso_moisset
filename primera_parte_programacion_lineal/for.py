'''realizar un programa que imprima por pantalla los numeros del 0 al 100 , este problema
ya lo pudimos resolver perfecto con el while, ahora lo que vamos a hacer es resolverlo con el for'''
'''el RANGE genera una lista de valores del numero que le pasamos -1 , por lo tanto si le ponemos 101 nos 
va a mostrar hasta el numero 100 '''

for x in range(101):
    print(x)
# print(x, end='-')
'''ahora si queremos por ejemplo mostar los numeros del 20 al 30 
en el range tenemos que indicarle ambos valores'''
for x in range(20, 31):
    print(x)

    '''tambien se le pueden pasar tres parametros al range '''

for x in range(1, 101, 2):  # en este caso es de 1 al 100 y nos muestra los impares porque el 2 corresponde a la secuencia
    print(x)
