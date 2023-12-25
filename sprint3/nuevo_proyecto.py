from abc import ABC, abstractmethod
import random

class Jugador(ABC):
    def __init__(self, nombre: str, simbolo: str) -> None:
        self.nombre = nombre
        self.simbolo = simbolo

    @abstractmethod
    def elegir_casilla(self, casilla) -> tuple[int, int]:
        pass

class JugadorHumano(Jugador):
    def elegir_casilla(self, casilla) -> tuple[int, int]:
        while True:
            try:
                x = int(input("Ingrese la coordenada horizontal (1-3): "))
                y = int(input("Ingrese la coordenada vertical (1-3): "))
                if 1 <= x <= 3 and 1 <= y <= 3 and casilla.es_valida(x, y):
                    return x, y
                else:
                    print("Casilla ocupada. Ingrese de nuevo")
            except ValueError:
                print("Error. Ingrese de nuevo")

class JugadorPC(Jugador):
    def elegir_casilla(self, casilla) -> tuple[int, int]:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        while not casilla.es_valida(x, y):
            x = random.randint(1, 3)
            y = random.randint(1, 3)
        return x, y

class Tablero:
    def __init__(self):
        self.casillas = {(x, y): ' ' for x in range(1, 4) for y in range(1, 4)}

    def marcar_casilla(self, x, y, simbolo):
        if self.es_valida(x, y):
            self.casillas[(x, y)] = simbolo
            return True
        return False

    def es_valida(self, x, y):
        return self.casillas[(x, y)] == ' '

    def hay_victoria(self):
        lineas = []

        for i in range(1, 4):
            lineas.append([(i, j) for j in range(1, 4)])
            lineas.append([(j, i) for j in range(1, 4)])
        lineas.append([(i, i) for i in range(1, 4)])
        lineas.append([(i, 4 - i) for i in range(1, 4)])

        for linea in lineas:
            simbolos = [self.casillas[posicion] for posicion in linea]
            if simbolos.count('X') == 3 or simbolos.count('O') == 3:
                return True
        return False

    def imprimir_tablero(self):
        for fila in range(1, 4):
            for columna in range(1, 4):
                print(self.casillas[(fila, columna)], end=' ')
                if columna < 3:
                    print('|', end=' ')
            print()
            if fila < 3:
                print('-' * 10) 

def jugar():
    print("TRES EN RAYA ")
    humano = JugadorHumano('Jugador Humano', 'X')
    pc = JugadorPC('Jugador PC', 'O')
    casilla = Tablero()

    for turno in range(1, 10):  
        if turno % 2 != 0:
            jugador = humano
        else:
            jugador = pc

        casilla.imprimir_tablero()
        print(f"\nTurno de {jugador.nombre} ({jugador.simbolo}):")

        x, y = jugador.elegir_casilla(casilla)
        casilla.marcar_casilla(x, y, jugador.simbolo)

        if casilla.hay_victoria():
            casilla.imprimir_tablero()
            print(f"\nGanador : {jugador.nombre} ({jugador.simbolo})")
            break

    else:
        print("\nNo hay ganadores")

if __name__ == "__main__":
    jugar()