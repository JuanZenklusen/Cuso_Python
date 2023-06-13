#Consiguna 3
print('Consigna 3:\n')

# Pedir variables
correctas = int(input('Ingrese cantidad de respuestas correctas: '))
incorrectas = int(input('Ingrese cantidad de respuestas incorrectas: '))
blanco = int(input('Ingrese cantidad de respuestas en blanco: '))

# calculo de puntaje
resultado = (correctas*3)-(incorrectas*1)+(blanco*0)

# imprimir en pantalla el resultado
print('El puntaje final es: ', resultado,'\n')