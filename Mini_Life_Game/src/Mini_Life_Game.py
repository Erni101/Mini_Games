# Juego de la Vida mejorado
import time
import copy
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_tablero(tablero, turno=None):
    if turno is not None:
        print(f"\nTurno {turno}")
    for fila in tablero:
        print("".join("@" if celula else "_" for celula in fila))
    print("-" * len(tablero[0]))

def contar_vecinas_vivas(matriz, x, y):
    filas, columnas = len(matriz), len(matriz[0])
    vecinos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    vivas = 0
    for dx, dy in vecinos:
        nx, ny = x + dx, y + dy
        if 0 <= nx < filas and 0 <= ny < columnas and matriz[nx][ny]:
            vivas += 1
    return vivas

def jugar(matriz, maximo_turnos, tiempo):
    for turno in range(1, maximo_turnos + 1):
        limpiar_pantalla()
        imprimir_tablero(matriz, turno)
        nuevo_tablero = copy.deepcopy(matriz)
        for x in range(len(matriz)):
            for y in range(len(matriz[0])):
                vecinas_vivas = contar_vecinas_vivas(matriz, x, y)
                if matriz[x][y] == 1:
                    if vecinas_vivas < 2 or vecinas_vivas > 3:
                        nuevo_tablero[x][y] = 0
                else:
                    if vecinas_vivas == 3:
                        nuevo_tablero[x][y] = 1
        if nuevo_tablero == matriz:
            print("El tablero no cambia más. Fin del juego.")
            break
        matriz = nuevo_tablero
        time.sleep(tiempo)

def menu():
    estado = True
    dicc = {
        'tiempo': 1,
        'max_turnos': 20,
        'tablero': [],
    }

    while estado:
        print('''
1) Establecer el tiempo entre turnos
2) Establecer el número máximo de turnos
3) Crear un tablero para el juego
4) Abandonar el juego
        ''')
        try:
            opcion = int(input('Elija una opción: '))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            try:
                dicc['tiempo'] = float(input("Establece el tiempo en segundos (puede ser decimal): "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == 2:
            try:
                dicc['max_turnos'] = int(input("Establece el número máximo de turnos: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == 3:
            try:
                filas = int(input("Número de filas: "))
                columnas = int(input("Número de columnas: "))
            except ValueError:
                print("Por favor, ingrese números válidos.")
                continue
            tablero = [[0] * columnas for _ in range(filas)]
            dicc['tablero'] = tablero

            while True:
                print('''
1) Cambiar el estado de una célula
2) Insertar varias células
3) Mostrar el tablero
4) Limpiar el tablero
5) Empezar el juego
6) Abandonar el tablero
                ''')
                try:
                    sub_opcion = int(input("Seleccione una opción: "))
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue

                if sub_opcion == 1:
                    try:
                        x = int(input("Coordenada X (fila): "))
                        y = int(input("Coordenada Y (columna): "))
                        if 0 <= x < filas and 0 <= y < columnas:
                            tablero[x][y] = 1 if tablero[x][y] == 0 else 0
                        else:
                            print("Coordenadas fuera de rango.")
                    except ValueError:
                        print("Por favor, ingrese números válidos.")
                elif sub_opcion == 2:
                    try:
                        n = int(input("¿Cuántas células deseas insertar? "))
                        for _ in range(n):
                            x = int(input("Coordenada X (fila): "))
                            y = int(input("Coordenada Y (columna): "))
                            if 0 <= x < filas and 0 <= y < columnas:
                                tablero[x][y] = 1
                            else:
                                print("Coordenadas fuera de rango.")
                    except ValueError:
                        print("Por favor, ingrese números válidos.")
                elif sub_opcion == 3:
                    imprimir_tablero(tablero)
                elif sub_opcion == 4:
                    tablero = [[0] * columnas for _ in range(filas)]
                    dicc['tablero'] = tablero
                    print("Tablero limpiado.")
                elif sub_opcion == 5:
                    jugar(tablero, dicc['max_turnos'], dicc['tiempo'])
                    break
                elif sub_opcion == 6:
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
        elif opcion == 4:
            print("¡Hasta luego!")
            estado = False
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

