class Apuesta:
  def __init__(self, nombre_completo, dni, fecha, nro_tiket, agencia, juego, nro, monto_apuesta):
    self.nombre_completo = nombre_completo
    self.dni = dni
    self.fecha = fecha
    self.nro_tiket = nro_tiket
    self.agencia = agencia
    self.juego = juego
    self.nro = nro
    self.monto_apuesta = monto_apuesta

  def Imprimir_ticket(self):
    return f'''
    --------- Detalle de la apuesta --------- 
        Agencia: {(self.agencia).upper()}
        Tipo de Sorteo: {self.juego}
    
    Nombre:............... {(self.nombre_completo).upper()}
    DNI:.................. {self.dni}
    Fecha:................ {self.fecha}
    Nro. Ticket:.......... {self.nro_tiket}
    Numero/s apostado/s:.. {self.nro}
    Valor ticket:......... $ {self.monto_apuesta}
    -----------------------------------------\n\n'''