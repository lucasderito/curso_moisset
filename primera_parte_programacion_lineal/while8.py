'''relizar un programa que imprima 25 terminos de la serie 11-22-33-44 etc '''
# hay muchas formas de resolver, yo hice 25 x 11 y me dio 275 y utilice ese valor como condicion en el while.


x = 11
while x <= 275:
    print(x, end='-')
    x = x + 11
