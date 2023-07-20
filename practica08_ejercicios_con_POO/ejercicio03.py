'''Crea una clase Estudiante que tenga atributos como nombre, edad y notas (una lista de calificaciones). 
Añade métodos para calcular el promedio de las notas y para determinar si el estudiante ha aprobado o no 
(promedio mayor o igual a 60).'''

class Estudiante:
  def __init__(self, nombre, edad, notas):
    self.nombre = nombre
    self.edad = edad
    self.notas = notas

  def Promedios(self):
    resultado = round(sum(self.notas)/len(self.notas),2)
    return f'Promedio de notas del alumno {self.nombre}: {resultado}'

estudiante1 = Estudiante('Juan Zenklusen', 20, [10,7,5])
estudiante2 = Estudiante('José Luis Boidi', 35, [10,10,10])

print(estudiante1.Promedios())
print(estudiante2.Promedios())
