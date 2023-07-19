'''Crea una clase Libro que tenga atributos como titulo, autor y año_publicacion. Añade métodos para mostrar la información del libro y para verificar si el libro es antiguo (publicado antes de 2000) o no.'''

#Creo la clase
class Libro:
  #Primero siempre el constructor y los atributos
  def __init__(self, titulo, autor, a_publicacion):
    self.titulo = titulo
    self.autor = autor
    self.a_publicacion = a_publicacion #año de publicacion

  #Declaro el método info
  def info(self):
    return f'El libro es {self.titulo}, su autor es {self.autor} y fue publicado en el año {self.a_publicacion}'

  #Declaro el método antiguo
  def antiguo(self):
    if self.a_publicacion < 2000:
      return f'Publicado antes del 2000'
    else:
      return f'Publicado después del 2000'

#Creo dos objetos para probar
libro = Libro('Los juegos del Hambre', 'Autorcito', 1990)
libro2 = Libro('Los juegos del Hambre en llamas', 'Autorcito', 2010)

#imprimo los métodos
print(libro.antiguo())
print(libro2.antiguo())
print(libro.info())
print(libro2.info())
