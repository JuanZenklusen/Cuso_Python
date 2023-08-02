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


menu = {
    '1': 'Quiniela',
    '2': 'Quini 6',
    '3': 'Comprobar apuesta',
    '4': 'Arqueo de caja',
    '5': 'Salir',
}