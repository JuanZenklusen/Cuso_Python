passw = input('Ingrese contraseña: ')
print('Contraseña guardada correctamente.\n')

check = input('ingrese su contraseña: ')

while check != passw:
  print('Contraseña incorrecta...\n')
  check = input('ingrese su contraseña: ')

print('Contraseña correcta, bienvenido!')
