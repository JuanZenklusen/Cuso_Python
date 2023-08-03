from datetime import date, timedelta

'''Crea una clase CuentaBancaria que tenga atributos como titular, saldo y interes. Añade métodos para depositar dinero en la cuenta, retirar dinero de la cuenta y calcular el saldo después de ciertos períodos de tiempo considerando el interés.'''

class CuentaBancaria:
  def __init__(self, titular, saldo, interes):
    self.titular = titular
    self.saldo = saldo
    self.interes = interes

  def VerDatos(self):
    return f'\nCuenta del cliente: {self.titular}\nSaldo actual: ${self.saldo}\nInterés aplicable: {self.interes}'

  def DepositarDinero(self):
    saldo_actual = self.saldo
    saldo_ingresado = float((input('\nIngrese monto a depositar: $')))
    nuevo_saldo = saldo_actual + saldo_ingresado
    self.saldo = nuevo_saldo

  def RetirarDinero(self):
    saldo_actual = self.saldo
    saldo_a_retirar = float((input('\nIngrese monto a depositar: $')))
    if saldo_a_retirar <= saldo_actual:
      nuevo_saldo = saldo_actual - saldo_a_retirar
      self.saldo = nuevo_saldo
    else:
      return print(f'No cuenta con el dinero suficiente') #ver como sacar el PRINT

  def CalcularInteres(self, y, m, a):
    fecha_de_hoy = date.today()
    fecha_de_calculo = date(y, m, a)
    diferencia = fecha_de_calculo - fecha_de_hoy
    saldo_a_fecha = round(self.saldo * (1 + (self.interes*(diferencia.days/365))),2)
    return saldo_a_fecha
    

cliente1 = CuentaBancaria('Juan Zenklusen', 15000, 0.4)

print(cliente1.VerDatos())
cliente1.DepositarDinero()
print(cliente1.VerDatos())
cliente1.RetirarDinero()
print(cliente1.VerDatos())

print('Calcular monto final segun la fecha:')
dia = int(input('Ingrese día: '))
mes = int(input('Ingrese mes: '))
año = int(input('Ingrese año: '))

print(f'Su saldo a la fecha será de: ${cliente1.CalcularInteres(2024, 7, 21)}')
