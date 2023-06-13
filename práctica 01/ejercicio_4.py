#Consiguna 4
print('Consigna 4:\n')

# Pedir variables
ganados = int(input('Ingrese cantidad de partidos ganados: '))
empatados = int(input('Ingrese cantidad de partidos empatados: '))
perdidos = int(input('Ingrese cantidad de partidos perdidos: '))

# calcular
puntos = (ganados*3)+empatados

# imprimir en pantalla el resultado
print('El total de puntos obtenidos por el club ABC fue de: ', puntos,'\n')