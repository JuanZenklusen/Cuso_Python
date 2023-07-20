'''Crear una clase Empleado que modele la información que una empresa mantiene
sobre cada empleado: código, sueldo base, pago por hora extra, horas extras
realizadas en el mes, casado o no y número de hijos.
Al crear objetos de esta clase se deberán proporcionar los datos de un empleado, y los
métodos deberán permitir realizar:
a) Cálculo sueldo incluyendo pago de horas extras.
b) Cálculo de retenciones. Suponer 5% si es casado y 5% por cada hijo
c) Cálculo del sueldo neto.
d) Mostrar el detalle de pago.'''

class Empleado:
  def __init__(self, codigo, sueldo_base, monto_hora_extra, horas_extras_trabajadas, estado_civil, cantidad_hijos):
    self.codigo = codigo
    self.sueldo_base = sueldo_base
    self.monto_hora_extra = monto_hora_extra
    self.horas_extras_trabajadas = horas_extras_trabajadas
    self.estado_civil = estado_civil
    self.cantidad_hijos = cantidad_hijos

  def Calcular_sueldo_con_hsextras(self):
    pass

  def Calcular_retenciones(self):
    pass

  def Calcular_sueldo_neto(self):
    pass

  def Mostrar_detalle_pago(self):
    pass