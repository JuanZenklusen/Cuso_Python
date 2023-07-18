#Consiguna 9
print('Consigna 9:\n')

# Ingresar datos
nombre = input('Nombre y apellido del empleado: ')
dni = input('Número de D.N.I.: ')
sueldo_basico = float(input('Ingrese sueldo básico: '))
antig = int(input('¿Cuántos años hace que trabaja?: '))
estado_civil = int(input('Estado civil: [0 si es soltero / 1 si es casado]: '))
hijos = int(input('Ingrese cantidad de hijos: '))
presentismo = int(input('¿Corresponde presentismo?: [1 si corresponde cobrar / 0 si no corresponde]'))

# cálculos
SB = sueldo_basico
antiguedad = SB*0.012*antig
if presentismo == 1:
  MP = 3500
else:
  MP = 0
AJ = SB*.11
OS = SB*.03
AG = SB*.01
if estado_civil == 1:
  conyuge = 800
else:
  conyuge = 0
hjs = hijos*400

SN = SB+antiguedad+MP-AJ-OS-AG+conyuge+hjs

# resultado en pantalla
print('\nRecibo de haberes de:', nombre, 'DNI:', dni)
print('Sueldo básico: $ ', SB)
if antig > 0:
  print(' + Antigûedad: $ ', antiguedad)
if presentismo > 0:
  print(' + Presentismo: $', MP)
if conyuge > 0:
  print(' + Conyugue: $', conyuge)
if hjs > 0:
  print(' + Hijo(s): $', hjs)
print(' - Aporte Jubilatorio: $', AJ)
print(' - Obra Social: $', OS)
print(' - Aporte Gremial: $', AG)
print('-----------------------')
print('Sueldo Neto: $', SN)