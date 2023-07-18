import math

#Consiguna 5
print('Consigna 5:\n')

# ingresar datos
tam_disco = float(input('¿Cuántos GB tiene tu disco? '))

# cálculo
cantidad_discos = math.ceil((tam_disco*1024)/1.44)

# resultados en pantalla
print('Se necesitan ', round(cantidad_discos), 'discos de 3.5\n')