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
    return self.a_publicacion < 2000

#Creo dos objetos para probar
libro = Libro('Los juegos del Hambre', 'Suzanne Collins', 2008)
libro2 = Libro('En llamas', 'Suzanne Collins', 2009)
libro3 = Libro('Sinsajo', 'Suzanne Collins', 2010)
libro4 = Libro('Balada de pajaros cantores y serpientes', 'Suzanne Collins', 2020)

#imprimo los métodos
'''print(libro.antiguo())
print(libro2.antiguo())
print(libro.info())
print(libro2.info())

Aqí hice una modificacion porque el profe lo resolvió distinto a la hora de generar el metodo de 'antiguo' ya que hizo directo el return y no dejo el if.

'''

libros = [libro, libro2, libro3, libro4]

for lib in libros:
  print(lib.info())
  if lib.antiguo():
    print('El libro es antiguo')
  else:
    print('El libro es nuevo')