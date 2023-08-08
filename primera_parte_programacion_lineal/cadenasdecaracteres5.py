"""Ingresar una oracion que pueden tener letras tanto en mayusculas como en minusculas,
 contar la cantidad de vocales.
 Crear un segundo string con toda la oracion en minuscula para que sea mas facil diponer la condicion
 que verifica que es una vocal """

oracion = input("Ingrese una oracion que puede contener mayusculas o minusculas :")
oracion_minuscula = oracion.lower()
x = 0
contador_vocales = 0
while x < len(oracion_minuscula):
    if oracion_minuscula[x] == 'a' or oracion_minuscula[x] == 'e' or oracion_minuscula[x] == 'i' or oracion_minuscula[
        x] == 'o' or oracion_minuscula[x] == 'u':
        contador_vocales += 1
    x += 1
print(f"La cantidad de vocales es de :{contador_vocales}")
