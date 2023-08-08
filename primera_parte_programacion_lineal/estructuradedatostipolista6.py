"""definir una lista que almacene por asignacion el nombre de 5 personas.
contar cuantos de esos nombres tienen 5 o mas caracteres"""

lista = ['luc', 'luisina', 'bian', 'homero', 'chichita']
x = 0
contador = 0
while x < len(lista):
    if len(lista[x]) >= 5:
        contador += 1
    x += 1
print(f"La cantidad de nombres que tienen 5 o mas caracteres es :{contador}")
