numero = int(input("Ingrese un número entero: "))
resul = True

if numero < 2:
    resul = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            resul = False
            break

if resul:
  print('El numero es primo')
else:
  print('El numero no es primo')
