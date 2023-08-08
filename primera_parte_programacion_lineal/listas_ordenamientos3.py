"""Crear una lista y almacenar los nombres de 5 paises.
Ordenar alfabeticamente la lista e imprimirla."""

lista_paises = []
for x in range(5):
    pais = input('Ingrese el pais :')
    lista_paises.append(pais)
print(f'La lista de paises ingresadas es :{lista_paises} ')
for k in range(4):  # for para ordenar todos los numeros , tamano de lista - 1 porque es una comparacion menos que la cantidad de valores
    for x in range(4):
        if lista_paises[x] > lista_paises[x + 1]:
            aux = lista_paises[x]
            lista_paises[x] = lista_paises[x + 1]
            lista_paises[x + 1] = aux
print(f' La lista ordenada alfabeticamente es : {lista_paises}')
