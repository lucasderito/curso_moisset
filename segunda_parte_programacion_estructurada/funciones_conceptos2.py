"""Confeccionar una aplicacion que solicite la carga de dos valores enteros y muestre su suma.
repetir la carga e impresion de la suma 5 veces.
Mostrar una linea separadora despues de cada vez que cargamos dos valores y se suma
"""


def carga_suma():
    n1 = int(input('Ingrese el primer valor :'))
    n2 = int(input('Ingrese el segundo valor :'))
    suma = n1 + n2
    print(f'La suma de los valores es : {suma}')

def linea_separadora():
    print('--------------------------------------------------------------------------------')


# BLOQUE PRINCIPAL
# DENTRO DEL BLOQUE PRINCIPAL PODEMOS LLAMAR A LAS FUNCIONES DE DIFERENTES MANERAS , POR EJEMPLO
# PODEMOS LLAMARLA CON UN CICLO REPETITIVO COMO A CONTINUACION

# COMO EL ENUNCIADO DICE QUE HAY QUE LLAMARLA 5 VECES , PODRIAMOS HACER 5 LLAMADOS A carga_suma
"""
carga_suma()
carga_suma()
carga_suma()
carga_suma()
carga_suma()
"""
# PERO LA FORMA ADECUADA DE HACERLO SERIA ASI
for x in range(5):
    carga_suma() # aca llamamos a la funcion para que sume
    linea_separadora() # aca llamamos a la funcion linea separadora