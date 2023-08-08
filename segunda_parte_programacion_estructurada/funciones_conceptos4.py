"""Desarrollar un programa que solicite la carga de tres valores y muestre el menor.
Desde el bloque principal del programa llamar dos veces a dicha funcion sin usar
una estructura repetitiva"""


def numero_menor():
    n1 = int(input('Ingrese el primer valor :'))
    n2 = int(input('Ingrese el segundo valor :'))
    n3 = int(input('Ingrese el tercer valor :'))
    if n1 < n2 and n1 < n3:
        print(f'{n1} es el menor valor :')
    elif n2 < n1 and n2 < n3:
        print(f'{n2} es el menor valor :')
    elif n3 < n1 and n3 < n2:
        print(f'{n3} es el menor valor :')
    else:
        print('Hay numeros iguales no se puede determinar el menor valor')
# le agrege el condicional de numeros iguales para agotar todas las posibilidades ya que si ingresaba
# dos numeros menores iguales no me devolvia el menor valor .

# BLOQUE PRINCIPAL
numero_menor()
numero_menor()
