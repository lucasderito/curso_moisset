"""Vimos en el concepto anterior que una funcion resuelve una parte de nuestro algoritmo
Tenemos por un lado la declaracion de una funcion por medio de un nombre y el algoritmo de la funcion
seguidamente. Luego para que se ejecute la funcion la llamamos desde el bloque principal de nuestro programa.
Ahora veremos que una funcion puede tener parametros para recibir datos.
Los parametos nos permiten comunicarle algo a la funcion y la hace mas flexible.
Una funcion con parametros nos hace mas flexible la misma para utilizarla en distintas circunstancias
"""
""" PROBLEMA A RESOLVER :
1- Confeccionar una aplicacion que muestre una presentacion en pantalla del programa.
2- Solicite la carga de dos valores y nos muestre la suma
3- Mostrar finalmente un mensaje de despedida del programa.

vamos a hacer las funciones de bienvenida y despedida en una misma funcion
"""

def mostrar_mensaje (mensaje): # aca definimos el mostrar mensaje por parametro al ponerle algo adentro
    print('------------------------------------------------------')
    print(mensaje) # aca lo mismo.
    print('------------------------------------------------------')


def carga_suma():
    n1 = int(input('Ingrese el primer valor :'))
    n2 = int(input('Ingrese el segundo valor :'))
    suma = n1 + n2
    print(f'La suma de los valores es : {suma}')

#BLOQUE PRINCIPAL
mostrar_mensaje('El programa calcula la suma de dos valores ingresados por teclado')
#como vemos en la linea de arriba tenemos llamamos a una funcion pero el mensaje se lo pasamos
# por parametro dentro del mismo llamado. Por lo tanto es mas versatil porque nos permite poner el
#mensaje que nosotros queremos en el momento de la llamada desde aca , osea desde el bloque principal
carga_suma()
mostrar_mensaje('Gracias por utilizar este programa')
# aca de nuevo como es un mensaje de despedida ponemos el mensaje aca y llamamos por parametro a la funcion
# le pasamos por parametro lo que queremos que diga