""" Solicitar un ingreso de una clave por teclado y almacenarla en una cadena de caracteres
Controlar que el string tenga entre 10 y 20 caracteres para que sea valida
Caso contrario mostrar un mensaje de error """

clave = input("Ingrese una clave :")

x = 0
if len(clave) >= 10 and len(clave) <= 20:
    print("El largo de la clave es correcto")
else:
    print("error")
