nombre_largo = input('Escribe tu nombre: ')
length = len(nombre_largo)

print(f'Mucho gusto {nombre_largo}, tu nombre contiene {length} letra{ "s" if length > 1 else "" }.')
