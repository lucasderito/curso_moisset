'''se carga una fecha , dia , mes y anio, por teclado, mostrar un mensaje si corresponde al primer
trimestre del anio ( enero , febrero , marzo). UTILIZANDO ======OR======= '''

dia = int(input("Ingrese dia :"))
mes = int(input("Ingrese mes :"))
anio = int(input("Ingrese el anio :"))
if mes == 1 or mes == 2 or mes == 3:
    print("La fecha ingresada corresponde al primer trimestre del anio :")
else:
    print("La fecha ingresada no corresponde al primer trimestre del anio")




'''ESTE EJEMPLO ES PARA VER EL CONDICIONAL OR , NO RESUELVE EL PROBLEMA DE MANERA OPTIMA .. OPTIMO SERIA PREGUNTAR 
SI MES ES <=3 '''