""" los string en python son inmutables , quiere decir que una vez que los inicializamos no podemos modificar
su contenido
osea si tengo definido :
nombre = 'juan'
no puedo hacer lo siguiente
nombre[0] = n
osea que no puedo cambiar parte de ese string

lo que si se puede hacer es asignarle otro string a la misma variable.. osea
nombre = 'juan'
print(nombre)
nombres = 'ana'
print(ana)

los string tienen una serie de metodos que nos facilitan la creacion de nuestro programa
los primeros 3  metodos que veremos son :
upper() : devuelve una cadena de caracteres todos convertidos a mayusculas
lower() : devuelve una cadena de caracteres todos convertidos a minusculas
capitalize : devuelve una cadena de caracteres con la primer letra en mayuscula y el resto en minuscula.
"""

""" ejemplo .. inicializamos un string con  la cadena 'mAria' luego llamamos a los metodos """

nombre = ('lUcAs')
print (nombre)
nombre_con_upper = nombre.upper() # llamamos al metodo , lo guardamos en otra variable
print(nombre_con_upper) #imprimimos
nombre_con_lower = nombre.lower()# llamamos al metodo , lo guardamos en otra variable
print(nombre_con_lower)#imprimimos
nombre_con_capitalize = nombre.capitalize()# llamamos al metodo , lo guardamos en otra variable
print(nombre_con_capitalize)#imprimimos