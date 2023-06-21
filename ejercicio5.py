monto = float(input('Ingrese cantidad a invertir: $ '))
interes = float(input('Ingrese interes anual: '))
year = int(input('Ingrese cantidad de años: '))
i=1
for i in range(1,year+1):
  print('En el año', i, 'el capital obtenido es: $', monto*(1+(interes/100))*i)
  i=i+1
