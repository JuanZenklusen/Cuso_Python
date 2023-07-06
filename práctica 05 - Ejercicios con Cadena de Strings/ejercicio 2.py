#Hay dos maneras de resolver: 
palabra=input('Ingrese una palabra: ')
print(palabra[::-1])

#o usando un for
palabra=input('Ingrese una palabra o frase: ')
for i in range(1,len(palabra)+1):
  print(palabra[-i], end="")