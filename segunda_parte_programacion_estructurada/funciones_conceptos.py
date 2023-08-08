"""Hasta ahora hemos trabajado con una metodologia de programacion lineal. Esto quiere decir que
todas las instrucciones de nuestro archivo *.py se ejecutan de forma secuencial de principio a fin.
Esta forma de organizar un programa puede ser llevado a cabo si el mismo es muy pequenio ( decenas de lineas)
Cuando los problemas a resolver tienden a ser mas grandes, la metodologia de programacion lineal,se vuelve
ineficiente y compleja.
EL SEGUNDO PARADIGMA DE LA PROGRAMACION QUE VEREMOS ES EL DE PROGRAMACION ESTRUCTURADA.
La programacion estructurada busca dividir o descomponer un problema complejo en pequenos problemas.
La solucion de cada uno de esos pequenos problemas nos trae la solucion del problema complejo.
En python el planteo de esas pequenas soluciones al problema complejo se hace dividiendo
el programa en FUNCIONES
Una funcion es un conjunto de instrucciones en Python que resulve un problema especifico.
El lenguaje python ya tiene incorporada algunas de esas funciones basicas, hasta ahora trabajamos con
algunas como por ejemplo , print , len , range.
VEAMOS AHORA COMO CREAR NUESTRAS PROPIAS FUNCIONES.
Los primeros problemas que presentaremos nos puede parecer que sea mas conveniente usar programacion
lineal en lugar de programacion estructurada por funciones.
A medida que avancemos veremos que si un programa empieza a ser mas complejo (cientos o miles de lineas)
la division en pequenas funciones nos permitira tener un programa mas ordenado y facil de entender y
por lo tanto de mantener."""

"""PROBLEMA A RESOLVER con las siguientes funciones:
1-Confeccionar una aplicacion que nos muestre una presentacion en pantalla del programa.
2-Solicite la carga de dos valores y nos muestre la suma.
3-Mostrar finalmente un mensaje de despedida del programa.
Implementar estas acciones en tres funciones.
"""


# PARA DEFINIR UNA FUNCION EN PYTHON TENEMOS LA PALABRA CLAVE DEF seguido del nombre de la funcion y ():

# PRIMERA FUNCION 1-
def presentacion():
    print("-------------------BIENVENIDOS---------------------")
    print('Programa que permite cargar por teclado por valor')
    print('Efectua la suma de los valores')
    print('Muestra el resultado de la suma')
    print('---------------------------------------------------')


# SEGUNDA FUNCION 2-
def carga_suma():
    n1 = int(input('Ingrese el primer valor :'))
    n2 = int(input('Ingrese el segundo valor :'))
    suma = n1 + n2
    print(f'La suma de los valores es : {suma}')

#TERCE FUNCION 3-
def finalizacion():
    print('---------------------------------------------------')
    print("-------------------GRACIAS POR UTILIZAR NUESTRO PROGRAMA---------------------")


# ACA ES EL BLOQUE PRINCIPAL DEL PROGRAMA DONDE VAMOS A LLAMAR NUESTRAS FUNCIONES.
presentacion() # asi se llama las funciones. Simple. El nombre de la funcion tal cual y ()
carga_suma() # aca llamamos a la segunda funcion.
finalizacion()# aca llamamos a la funcion de finalizacion

# IMPORTANTE !!!!!! EL ORDEN EN QUE SE LLAMA A LAS FUNCIONES INFLUYE EN EL PROGRAMA, POR LO TANTO
# DEBEMOS MANTENER EL ORDEN EN QUE LLAMAMOS LAS FUNCIONES
