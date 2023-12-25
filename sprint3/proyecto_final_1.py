from abc import ABC, abstractmethod
import random

class Jugador (ABC):
    def __init__(self, nombre : str, simbolo: str) -> None:
        self.nombre = nombre
        self.simbolo = simbolo
        
    @abstractmethod
    def elegir_casilla(self) -> tuple[int,int]:
        pass

class JugadorHumano(Jugador):
    def elegir_casilla(self) -> tuple[int,int]:
        x = int(input("Ingrese la coordenada vertical de la posición a marcar"))
        y = int(input("Ingrese la coordenada horizontal de la posición a marcar"))
        return x,y
    
class JugadorPC(Jugador):
    def elegir_casilla(self) -> tuple[int,int]:
        x = random.randint(1, 4)
        y = random.randint(1, 4)
        return x,y
    
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

        # Generar líneas horizontales y verticales
        for i in range(1, 4):
            lineas.append([(i, j) for j in range(1, 4)])
            lineas.append([(j, i) for j in range(1, 4)])

        # Generar líneas diagonales
        lineas.append([(i, i) for i in range(1, 4)])
        lineas.append([(i, 4 - i) for i in range(1, 4)])

        # Verificar si hay una línea ganadora en el tablero
        for linea in lineas:
            simbolos = [self.casillas[posicion] for posicion in linea]
            if simbolos.count('X') == 3 or simbolos.count('O') == 3:
                return True
        return False

    def imprimir_tablero(self):
        for fila in range(1, 4):
            for columna in range(1, 4):
                print(self.casillas[(fila, columna)], end=' ')
            print()

print("TRES EN RAYA")

