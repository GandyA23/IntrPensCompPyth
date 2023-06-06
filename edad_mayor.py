nombre_1 = input('Escribe tu nombre: ')
edad_1 = int(input(f'Escribe tu edad {nombre_1}: '))

nombre_2 = input('Escribe tu nombre: ')
edad_2 = int(input(f'Escribe tu edad {nombre_2}: '))

if edad_1 > edad_2:
    print(f'{nombre_1} es mayor que {nombre_2}.')
elif edad_2 > edad_1:
    print(f'{nombre_2} es mayor que {nombre_1}.')
else:
    print(f'{nombre_1} y {nombre_2} tienen la misma edad.')
