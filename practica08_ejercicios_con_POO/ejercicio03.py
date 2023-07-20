'''Crea una clase Estudiante que tenga atributos como nombre, edad y notas (una lista de calificaciones). 
Añade métodos para calcular el promedio de las notas y para determinar si el estudiante ha aprobado o no 
(promedio mayor o igual a 60).'''

class Estudiante:
  def __init__(self, nombre, edad, notas):
    self.nombre = nombre
    self.edad = edad
    self.notas = notas

  def Promedios(self):
    resultado = round(sum(self.notas)/len(self.notas),1)
    return resultado

  def Aprobar(self):
    if self.Promedios() > 6.0:
      return f'Aprobado'
    else:
      return f'Reprobado'

estudiante1 = Estudiante('Juan Zenklusen', 20, [10,7,5])
estudiante2 = Estudiante('José Luis Boidi', 35, [2,5,6])

print(f'El estudiante {estudiante1.nombre} tiene de promedio {estudiante1.Promedios()}. El curso ha sido {estudiante1.Aprobar()}')
print(f'El estudiante {estudiante2.nombre} tiene de promedio {estudiante2.Promedios()}. El curso ha sido {estudiante2.Aprobar()}')
