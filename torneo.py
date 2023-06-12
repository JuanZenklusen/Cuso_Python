import random

clubes = ['San Lorenzo', 'River', 'Boca', 'Racing', 'Independiente', 'Huracán', 'Newel`s', 'Rosario Central']

cantidad_clubes = len(clubes)
a1 = 1
a2 = (len(clubes)//2)+1

#random.shuffle(clubes)

print(clubes)

fecha = 1

for i in range(0,len(clubes)-1):
  print('\nFecha', fecha, '\n', clubes[0], 'vs', clubes[a1])
  print('', clubes[2], 'vs', clubes[a1+2])
  fecha = fecha +1
  '''  try:
    print('\nFecha', fecha, '\n', clubes[a2], 'vs', clubes[0],)
  except:
    print('')'''
  a1=a1+1
  a2=a2+1
