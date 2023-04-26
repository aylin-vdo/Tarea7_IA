import copy
import math

from numpy import empty


def minimax(tablero, jugador, profundidad, profundidad_max):
    if profundidad == profundidad_max or checar_gano(tablero):
        return evaluar(tablero)

    mejor_puntaje = -math.inf if jugador == 1 else math.inf
    for movim in traer_mov_posibles(tablero):
        nuevo_tab = hacer_mov(tablero, jugador, movim)
        puntaje = minimax(nuevo_tab, -jugador, profundidad + 1, profundidad_max)
        if puntaje is None:
            puntaje = -math.inf if jugador == 1 else math.inf
        if jugador == 1:
            mejor_puntaje = max(mejor_puntaje, puntaje)
        else:
            mejor_puntaje = min(mejor_puntaje, puntaje)

    return mejor_puntaje


def checar_gano(tablero):
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != 0:
            return fila[0]

    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != 0:
            return tablero[0][col]

    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != 0:
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != 0:
        return tablero[0][2]

    return 0

def checar_lleno(tablero):
    for fila in tablero:
        if 0 in fila:
            return False
    return True

def traer_mov_posibles(tablero):
    movimientos = []
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == 0:
                movimientos.append((fila, col))
    return movimientos

def hacer_mov(tablero, jugador, movim):
    row, col = movim
    nuevo_tab = copy.deepcopy(tablero)
    nuevo_tab[row][col] = jugador
    return nuevo_tab

def evaluar(tablero):
    ganador = checar_gano(tablero)
    if ganador == 1:
        return 1
    elif ganador == -1:
        return -1
    elif checar_lleno(tablero):
        return 0
    else:
        return None


def mostrar_tablero(tablero):
    print("   0  1  2")
    for fila in range(3):
        print(fila, end='  ')
        for col in range(3):
            if tablero[fila][col] == 1:
                print("X ", end='')
            elif tablero[fila][col] == -1:
                print("O ", end='')
            else:
                print("- ", end='')
        print()

def jugar():
    tablero = [[0 for j in range(3)] for i in range(3)]
    jugador_actual = 1
    while not checar_gano(tablero) and not checar_lleno(tablero):
        mostrar_tablero(tablero)
        print("Turno de jugador", jugador_actual)
        if jugador_actual == 1:
            mejor_puntaje = -math.inf
            for movim in traer_mov_posibles(tablero):
                nuevo_tab = hacer_mov(tablero, jugador_actual, movim)
                puntaje = minimax(nuevo_tab, -jugador_actual, profundidad=0, profundidad_max=100)
                if puntaje > mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejor_mov = movim
            tablero = hacer_mov(tablero, jugador_actual, mejor_mov)
        else:
            mejor_puntaje = math.inf
            for movim in traer_mov_posibles(tablero):
                nuevo_tab = hacer_mov(tablero, jugador_actual, movim)
                puntaje = minimax(nuevo_tab, -jugador_actual, profundidad=0, profundidad_max=5)
                if puntaje < mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejor_mov = movim
            tablero = hacer_mov(tablero, jugador_actual, mejor_mov)
        jugador_actual *= -1

    mostrar_tablero(tablero)
    ganador = checar_gano(tablero)
    if ganador:
        print("Jugador", ganador, "Gana!")
    else:
        print("Empate")

def jugar_vs_compu_hprimero():
    tablero = [[0 for j in range(3)] for i in range(3)]
    jugador_actual = 1
    while not checar_gano(tablero) and not checar_lleno(tablero):
        mostrar_tablero(tablero)
        print("Turno de jugador", jugador_actual)
        if jugador_actual == 1:
            mov_val = False
            while not mov_val:
                movim = input("Ingresa las coordenadas de tu movimiento separadas por una coma (por ejemplo: 0,2): ")
                movim = movim.split(',')
                movim = [int(x.strip()) for x in movim]
                mov_val = True
            tablero = hacer_mov(tablero, jugador_actual, movim)
        else:
            mejor_puntaje = -math.inf
            for movim in traer_mov_posibles(tablero):
                nuevo_tab = hacer_mov(tablero, jugador_actual, movim)
                puntaje = minimax(nuevo_tab, -jugador_actual, profundidad=0, profundidad_max=100)
                if puntaje > mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejor_mov = movim
            tablero = hacer_mov(tablero, jugador_actual, mejor_mov)
        jugador_actual *= -1

    mostrar_tablero(tablero)
    ganador = checar_gano(tablero)
    if ganador:
        print("Jugador", ganador, "Gana!")
    else:
        print("Empate")

def jugar_vs_compu():
    tablero = [[0 for j in range(3)] for i in range(3)]
    jugador_actual = 1
    while not checar_gano(tablero) and not checar_lleno(tablero):
        mostrar_tablero(tablero)
        print("Turno de jugador", jugador_actual)
        if jugador_actual == 1:
            mejor_puntaje = -math.inf
            for movim in traer_mov_posibles(tablero):
                nuevo_tab = hacer_mov(tablero, jugador_actual, movim)
                puntaje = minimax(nuevo_tab, -jugador_actual, profundidad=0, profundidad_max=100)
                if puntaje > mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejor_mov = movim
            tablero = hacer_mov(tablero, jugador_actual, mejor_mov)
        else:
            mov_val = False
            while not mov_val:
                movim = input("Ingresa las coordenadas de tu movimiento separadas por una coma (por ejemplo: 0,2): ")
                movim = movim.split(',')
                movim = [int(x.strip()) for x in movim]
                mov_val = True
            tablero = hacer_mov(tablero, jugador_actual, movim)
        jugador_actual *= -1

    mostrar_tablero(tablero)
    ganador = checar_gano(tablero)
    if ganador:
        print("Jugador", ganador, "Gana!")
    else:
        print("Empate")


if __name__ == '__main__':
    jugar_vs_compu()