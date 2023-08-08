"""Crear y cargar en una lista los nombres de 5 paises y en otra lista paralela
la cantidad de habitantes del mismo. Ordenar alfabeticamente e imprimir los resultados.
Por ultimo ordenar con respecto a la cantidad de habitantes, ( de mayor a menor ) e imprimir nuevamente
"""

lista_paises = []
lista_habitantes = []
for x in range(5):
    pais = input('Ingrese el nombre del pais :')
    lista_paises.append(pais)
    habitantes = int(input('Ingrese la cantidad de habitantes :'))
    lista_habitantes.append(habitantes)
for f in range(4):
    for x in range(4):
        if lista_paises[x] > lista_paises[x + 1]:
            aux_pais = lista_paises[x]
            lista_paises[x] = lista_paises[x + 1]
            lista_paises[x + 1] = aux_pais
            aux_habitantes = lista_habitantes[x]
            lista_habitantes[x]= lista_habitantes[x + 1]
            lista_habitantes[x +  1] = aux_habitantes
print(' Listado de paises ordenados alfabeticamente ( incluye sus habitantes):')
for p in range(5):
    print(lista_paises[p], lista_habitantes[p])
# Por ultimo ordenar con respecto a la cantidad de habitantes, ( de mayor a menor ) e imprimir nuevamente
for f in range(4):
    for x in range(4):
        if lista_habitantes[x] < lista_habitantes[x + 1]:
            aux_habitantes = lista_habitantes[x]
            lista_habitantes[x] = lista_habitantes[x + 1]
            lista_habitantes[x + 1] = aux_habitantes
            aux_pais = lista_paises[x]
            lista_paises[x] = lista_paises[x + 1]
            lista_paises[x + 1] = aux_pais
print('Ordenamiento con respecto a la cantidad de habitantes de mayor a menor :')
for p in range(5):
    print(lista_habitantes[p], lista_paises[p])
