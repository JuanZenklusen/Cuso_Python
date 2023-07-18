import math

#Consiguna 6
print('Consigna 6:\n')

# ingresar datos
x1 = int(input('Ingrese posición inicial en el eje "x": '))
y1 = int(input('Ingrese posición inicial en el eje "y": '))

x2 = int(input('Ingrese posición final en el eje "x": '))
y2 = int(input('Ingrese posición final en el eje "y": '))

# calculo
delta_x = abs(x1-x2)
delta_y = abs(y1-y2)

hipotenusa = math.sqrt((delta_x**2)+(delta_y**2))

# resultados en pantalla
print('la distancia recorrida es: ', hipotenusa,'\n')