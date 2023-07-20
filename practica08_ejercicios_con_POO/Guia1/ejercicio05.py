'''Crea una clase Rectangulo que tenga atributos como largo y ancho. Añade métodos
para calcular el área, el perímetro y determinar si el rectángulo es cuadrado (largo
igual a ancho).'''

class Rectangulo:
  def __init__(self,largo,ancho):
    self.largo = largo
    self.ancho = ancho

  def Calcular_area(self):
    return self.largo * self.ancho

  def Calcular_perimetro(self):
    return self.largo*2 + self.ancho*2

  def Es_cuadrado(self):
    if self.largo == self.ancho:
      return f'Cuadrado'
    else:
      return f'Rectángulo'

rectangulo1 = Rectangulo(10,10)
print(f'El área es: {rectangulo1.Calcular_area()}')
print(f'El perímetro es: {rectangulo1.Calcular_perimetro()}')
print(f'Se trata de un: {rectangulo1.Es_cuadrado()}')
