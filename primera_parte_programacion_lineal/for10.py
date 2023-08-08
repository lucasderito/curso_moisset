'''realizar un programa que lea los lados de N triangulos e informar :
a) de cada uno de ellos  que tipo de triangulo es , equilatero ( tres lados iguales )
isoceles (dos lados iguales ) , escaleno (ningun lado igual ).
b)cantidad de triangulos de cada tipo '''

equilatero = 0
isoceles = 0
escanelos = 0
n_triangulos = int(input("Ingrese la cantida de triangulos que quiere procesar :"))
for f in range(n_triangulos):
    lado1 = int(input("Ingrese primer lado :"))
    lado2 = int(input("Ingrese primer lado :"))
    lado3 = int(input("Ingrese primer lado :"))
    if lado1 == lado2 and lado1 == lado3:
        equilatero += 1
        print("El triangulo es equilatero")
    elif lado1 == lado2 or lado1 == lado3:
        isoceles += 1
        print("El triangulo es isoceles")
    else:
        escanelos += 1
        print("El triangulo es escanelo")
print(f"La cantidad de triangulos equilateros es de : {equilatero}")
print(f"La cantidad de triangulos isoceles es de : {isoceles}")
print(f"La cantidad de triangulos escanelos es de : {escanelos}")
