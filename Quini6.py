import random

bolas = [0]
orden = ['primer', 'segunda', 'tercer', 'cuarta', 'quinta', 'sexta']

while len(bolas) <= 45:
  bolas.append(int(max(bolas)+1))

random.shuffle(bolas)

for i in range(0,6):
  print('La', orden[i], 'bola es:', bolas[i])
