'''confeccionar un programa que lea N pares de datos , cada par de datos corresponde a la medida
de la base y la altura de un triangulo, el programa debera informar :
a ) de cada triangulo la medida de su base , su altura y su superficie (la superficie de esta
se calcula con el producto de la base por la altura sobre 2 , osea base * altura / 2
b)La cantidad de triangulos cuya superficie es mayor a 12 '''

cantidad_de_triangulos_mayores = 0
n = int (input(" Ingrese cuantos triangulos ingresara :"))
for f in range(n):
    base = float (input("Ingrese la base del triangulo :"))
    altura = float (input("Ingrese la altura del triangulo :"))
    superficie_del_triangulo = base * altura / 2
    print(f"La base del triangulo es :{base}")
    print(f"La altura del triangulo es : {altura}")
    print(f"La superficie del triangulo es : {superficie_del_triangulo}")
    if superficie_del_triangulo > 12:
        cantidad_de_triangulos_mayores +=1
print(f"la cantidad de triangulos con superficie mayor a 12 es de : {cantidad_de_triangulos_mayores}")

