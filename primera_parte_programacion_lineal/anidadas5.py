'''un postulante a un empleo, realiza un test de capacitacion, se obtuvo la siguiente informacion
cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contesto correctamente
. Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo segun
el porcentaje de respuesta correcta que ha obtenido y sabiendo que :
niveles
maximo >=90%
medio >=75% y <90%
regular >=50% y <75%
fuera de nivel porcentaje<50%'''

total_preguntas = int(input("Ingrese la cantidad de preguntas que se le realizo al postulante :"))
respuestas_correctas = int(input("Ingrese la cantidad de respuestas correctas :"))
porcentaje = (respuestas_correctas * 100) / total_preguntas
if porcentaje >= 90:
    print(f"El nivel obtenido es el MAXIMO ya que obtuvo un {porcentaje}% de respuestas correctas")
elif porcentaje >= 75:
    print(f"El nivel obtenido es MEDIO ya que obtuvo un {porcentaje}% de respuestas correctas")
elif porcentaje >= 50:
    print(f"El nivel obtenido es REGULAR ya que obtuvo un {porcentaje}% de respuestas correctas")
else:
    print(f"El nivel obtenido esta FUERA DE NIVEL ya que obtuvo un {porcentaje}% de respuestas correctas")
