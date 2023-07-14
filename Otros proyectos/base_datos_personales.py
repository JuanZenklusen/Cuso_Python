bd = ['Juan Ignacio', 'Zenklusen', 35222582, '30/05/2023', 'San Cristóbal', 'Rafaela']

datos = {
  'apellido' : bd[1],
  'nombre' : bd[0],
  'dni' : bd[2],
  'nacimiento' : bd[3],
  'localidad_nac' : bd[4],
  'localidad_residencia' : bd[5]
}


print(f'''Nombre completo: \t\t\t\t{datos.get('apellido').upper()}, {datos.get('nombre')}
Documento de identidad: \t\t{datos.get('dni')}
Fecha de nacimiento: \t\t\t{datos.get('nacimiento')}
Localidad de nacimiento: \t\t{datos.get('localidad_nac')}
Localidad de residencia: \t\t{datos.get('localidad_residencia')}
''')
