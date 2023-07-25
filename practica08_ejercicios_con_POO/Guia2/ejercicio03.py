'''
Supongamos que estamos construyendo un programa para una tienda de productos electrónicos. Podemos utilizar herencia para modelar diferentes tipos de productos electrónicos, como "Teléfono", "Tableta" y "Computadora", que heredan atributos y comportamientos comunes de una clase base "ProductoElectronico".
'''

class ProductoEletronico:
  def __init__(self, nombre, stock, precio):
    self.nombre = nombre
    self.stock = int(stock)
    self.precio = float(precio)

  def Cuotas_sin_interes(self):
    return f'6 cuotas sin interés de ${round(self.precio/6, 2)}'


class Telefono(ProductoEletronico):
  def __init__(self, nombre, stock, precio, mac):
    super().__init__(nombre, stock, precio)
    self.mac = mac

  def llamar(self, numero):
    return f'Estas llamando a {numero}'

class Tableta(ProductoEletronico):
  def __init__(self, nombre, stock, precio, pantalla):
    super().__init__(nombre, stock, precio)
    self.pantalla = pantalla

  def jugar(self, juego):
    return f'Estás jugando a {juego}'

producto1 = Telefono('Samsung A04', 20, 72000, 13516813543813)
producto2 = Tableta('GalaxyTab', 20, 90000, '10.3"')

print(producto1.Cuotas_sin_interes())
print(producto2.Cuotas_sin_interes())
print(producto1.llamar(3492311561))
print(producto2.jugar('Call of Duty Mobile'))
