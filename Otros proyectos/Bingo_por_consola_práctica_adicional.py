import random
s = [1] #Creo una lista con el primer elemento: el 1

#Se completa la lista de nros del 1 al 90
while len(s) < 90:
  s.append(int(max(s)+1))

#Se genera el aleatorio
random.shuffle(s)

#Inicia lógica de Bingo
hubo_ganador = False
n=0
while hubo_ganador == False:
  print('\nEl siguiente número es:', s[n], '\n')
  if hubo_ganador == False:
    preguntar = input('¿Hay ganador? ')
    if preguntar != "":
      hubo_ganador=True
      print('BIIINGOOOOO')
    else:
      n = n+1
