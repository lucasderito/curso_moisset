"""ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter @ """

mail = input("Ingrese su mail :")
contador = 0
x = 0 #variable para avanzar caracter a caracter
while x < len(mail): #el len devuelve la cantidad
    if mail[x] == '@':# aca estamos preguntando si la posicion X que va recorriendo es un @ y lo vamos almacenando en contado
        contador += 1
    x +=1
if contador == 1:
    print("el mail contiene solo un @")
elif contador == 0:
    print("el mail no contiene @")
else:
    print("el mail contiene mas de un @")