from quiniela import Quiniela
from quini6 import Quini6

def Encabezado():
    nombre_quiniela = "* Quiniela | 'L A S U E R T E' *"
    encabezado_menu = '|Escoja la opción deseada:|'
    for i in range(len(nombre_quiniela)):
        print('*', end="")
    print(f'\n{nombre_quiniela}')
    for i in range(len(nombre_quiniela)+1):
        print('*', end="")
    print()
    for i in range(len(encabezado_menu)):
        print('-', end="")
    print(f'\n{encabezado_menu}')
    for i in range(len(encabezado_menu)):
        print('-', end="")
    print('\n1 - Quiniela\n2 - Quini 6\n3 - Comprobar apuesta\n4 - Arqueo de caja\n5 - Salir\n')

Encabezado()

menu = {
    '1': Quiniela,
    '2': Quini6,
    '3': 'Comprobar apuesta',
    '4': 'Arqueo de caja',
    '5': 'Salir',
}