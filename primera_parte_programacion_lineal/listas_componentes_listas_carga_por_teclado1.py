"""ahora vamos a hacer listas con componentes en su interior que tambien son de tipo listas
En muchas situaciones debemos crear una nueva lista dentro de otra lista cargando los datos por teclado

problema:
Crear y cargar una lista con los nombres de 3 alumnos.
Cada alumno tiene 2 notas, almacenar las notas en una lista paralela.
Cada componente de la lista paralela debe ser tambien una lista con las dos notas.
Imprimir luego cada nombre y sus dos notas.
Si cargaramos los datos por ASIGNACION, deberia ser algo parecido a esto

lista_alumnos = ['Luisina', 'Lucas', 'Bianca', 'Homero']
lista_notas = [[10, 8],[8, 9],[5, 6], [6, 7]]

En la componente 0 de la lista_alumnos tenemos almacenados el nombre Luisina y como son listas paralelas
en la componente 0 de la lista_notas tenemos almacenados una lista con dos notas [10] y [8]
Nuestro objetivo como nos pide el problema es cargar los datos por teclado
"""
lista_alumnos = []
lista_notas = []
for f in range(4):
    alumno = input(('Ingrese el nombre del alumno :'))
    lista_alumnos.append(alumno)
    nota1 = int(input('Ingrese la primer nota :'))
    nota2 = int(input('Ingrese la segunda nota :'))
    lista_notas.append([nota1, nota2])
for x in range(4):
    print(lista_alumnos[x], lista_notas[x][0], lista_notas[x][1])
