"""
Utiliza el algoritmo de enumeración exhaustiva para buscar la raíz cuadrada de un número. 
"""
def enumaracion_exhaustiva(objetivo):
    algoritmo = 'Enumeración Exhaustiva'
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        return f'{algoritmo}: La raíz cuadrada de {objetivo} es {respuesta}.'
    else:
        return f'{algoritmo}: {objetivo} no tiene una raíz cuadrada exacta.'

"""
Utiliza el algoritmo de aproximación de soluciones para buscar la raíz cuadrada de un número o su aproximado. 
"""
def aproximacion(objetivo):
    algoritmo = "Aproximación"
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        return f'{algoritmo}: No se encontro la raíz cuadrada de {objetivo}.'
    else: 
        return f'{algoritmo}: La raíz cuadrada de {objetivo} es {respuesta}.'

"""
Utiliza el algoritmo de búsqueda binaria para buscar la raíz cuadrada de un número o su aproximado. 
"""
def busqueda_binaria(objetivo):
    algoritmo = "Búsqueda Binaria"
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    return f'{algoritmo}: La raíz cuadrada del {objetivo} es la {respuesta}'


if __name__ == '__main__':
    while True:
        opcMenu = input("""
Menú de Búsqueda de Raíces Cuadradas

Escoja un algoritmo de búsqueda
1.- Enumeración Exhaustiva
2.- Aproximación
3.- Búsqueda Binaria
4.- Salir del Programa

Escriba una opción [1-4]: """)

        algoritmo = None

        if opcMenu == '1':
            algoritmo = enumaracion_exhaustiva
        elif opcMenu == '2':
            algoritmo = aproximacion
        elif opcMenu == '3':
            algoritmo = busqueda_binaria
        elif opcMenu == '4':
            break
        else: 
            print("Opción invalida, favor de escoger un número entre 1 y 4")
            continue

        objetivo = int(input("Escribe un número: "))

        print(algoritmo(objetivo))
    
    print("Ha finalizado el programa correctamente.")
