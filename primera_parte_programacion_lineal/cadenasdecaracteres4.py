"""cargar una oracion por teclado y mostrar luego cuantos espacios en blanco se ingresaron
tener en cuenta que un espacio en blanco es igual a = ' ' , en cambio una cadena vacia es igual a  = ''
"""

oracion = input(" Ingrese una oracion :")
contador_espacios_en_blanco = 0
x = 0
while x < len(oracion):
    if oracion[x] == ' ':
        contador_espacios_en_blanco += 1
    x += 1
print(f"la cantidad de espacioes en blanco es de : {contador_espacios_en_blanco}")
