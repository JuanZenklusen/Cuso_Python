from math import pi

print('Consigna 2:\n')

# definir entradas
radio = float(input('Ingrese rádio de la superficie: '))
altura = float(input('Ingrese altura del cilindro: '))

# proceso
if altura > radio:
    volumen = (pi*(radio**2))*altura
    print('El volumen del cilindro es:', volumen)
    print('\n')
else:
    #area = pi*(radio**2)
    print('error')
    print('\n')