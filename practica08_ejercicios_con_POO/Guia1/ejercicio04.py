'''Crea una clase Tienda que tenga atributos como nombre de la tienda y productos (una lista de nombres de productos). Añade métodos para agregar productos a la tienda, mostrar la lista de productos y determinar si un producto específico está disponible en la
tienda.'''

class Tienda:
  def __init__(self, nombre_tienda, productos):
    self.nombre_tienda = nombre_tienda
    self.productos = productos

  def Mostrar_lista_productos(self):
    return self.productos
    '''print('\nLista de productos:')
    for element in self.productos:
      print(element)''' #esto sería en caso de agregar un bucle for para que imprima en pantalla iterablemente

  def Agregar_producto(self, producto):
    self.productos.append(producto)
    return f'Producto {producto} agregado'

  def esta_disponible(self, texto):
    return texto in self.productos

tienda1 = Tienda('Compumundohipermegared', ['Monitor 29"', 'Gabinete tradicional', 'Gabinete gamer', 'Mouse Óptico', 'Teclado mecánico'])

tienda2 = Tienda('Garbarino', ['Lavarropas', 'Microhondas', 'Cocina', 'Plancha'])

print(tienda1.Mostrar_lista_productos())
tienda1.Agregar_producto('Webcam')
print(tienda1.Mostrar_lista_productos())
print(tienda1.esta_disponible('Teclado mecánico'))
