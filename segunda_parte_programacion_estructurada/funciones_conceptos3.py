"""Desarrollar un programa con 2 funciones.
La primer funcion que solicite un entero y muestre el cuadrado de dicho valor.
La segunda funcion que solicite la carga de dos valores y muestre el producto de los mismos.
Llamar desde el bloque principal del programa a ambas funciones."""

def cuadrado_numero():
    numero = int(input('Ingrese un numero :'))
    cuadrado = numero ** 2
    print(f'El cuadrado de {numero} es {cuadrado}')

def producto_numeros():
    n1 = int(input('Ingrese el primer valor :'))
    n2 = int(input('Ingrese el segundo valor :'))
    producto = n1 * n2
    print(f'El producto de los numeros es : {producto}')

# BLOQUE PRINCIPAL
cuadrado_numero()
producto_numeros()