"""Confeccionar una funcion que reciba tres enteros y nos muestre el mayor de ellos.
La carga de los valores hacerlo por teclado en otra funcion"""


def mostrar_mayor(v1, v2, v3):
    print('El mayor numero de los tres es :')
    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    else:
        print(n3)


def cargar():
    numero1 = int(input('Ingrese el primer numero :'))
    numero2 = int(input('Ingrese el segundo numero :'))
    numero3 = int(input('Ingrese el tercer numero :'))
    mostrar_mayor(numero1, numero2, numero3)

# bloque principal

cargar()

# se crean las funciones de arriba hacia abajo y se llaman de abajo hacia arriba , como si se fuesen desapilando.
# por lo tanto en el bloque principal llamamos el cagar , que es la funcion que esta encima de ella y la funcion cargar
# llama a la funcion mostrar_valor, tomando los valores por parametros

