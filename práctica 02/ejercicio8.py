print('Consigna 8:\n')

#entradas:
cal_a_1 = float(input('Ingrese primer calificacion del estudiante 1: '))
cal_b_1 = float(input('Ingrese segunda calificacion del estudiante 1: '))
cal_c_1 = float(input('Ingrese tercera calificacion del estudiante 1: '))
cal_a_2 = float(input('Ingrese primer calificacion del estudiante 2: '))
cal_b_2 = float(input('Ingrese segunda calificacion del estudiante 2: '))
cal_c_2 = float(input('Ingrese tercera calificacion del estudiante 2: '))

#proceso
cal_final_1 = (cal_a_1 + cal_b_1 + cal_c_1) - min(cal_a_1, cal_b_1, cal_c_1)
cal_final_2 = (cal_a_2 + cal_b_2 + cal_c_2) - min(cal_a_2, cal_b_2, cal_c_2)

#salida
if cal_final_1 == cal_final_2:
  print('Ambos tienen la misma calificación')
else:
  if cal_final_1 > cal_final_2:
    print('El alumno 1 tiene una mayor calificacion con: ', cal_final_1)
  else:
    print('El alumno 2 tiene una mayor calificacion con: ', cal_final_2)