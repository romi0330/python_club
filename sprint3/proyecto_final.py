from abc import ABC, abstractmethod
import random
import string

class Jugador (ABC):
    def __init__(self, nombre : str, apellido: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        
    @abstractmethod
    def elegir_casilla(self) -> float:
        pass

class JugadorHumano(Jugador):
    def __init__(self, nombre : str, apellido: str) -> None:
        super(JugadorHumano, self).__init__(nombre, apellido)
    def elegir_casilla(self) -> float:
        x = int(input("Ingrese la coordenada vertical de la posición a marcar"))
        y = int(input("Ingrese la coordenada horizontal de la posición a marcar"))
        return x,y
    
class JugadorPC(Jugador):
    def __init__(self, nombre : str, apellido: str) -> None:
        super(JugadorPC, self).__init__(nombre, apellido)
    def elegir_casilla(self) -> float:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        return x,y
    
class Tablero():
    def __init__(self, casillas : str) -> None:
        self.casillas = {(x,y):''}
    def marcar_casilla(self, x, y, simbolo):
        self.casillas[(x,y)] = simbolo
    def es_valida(self,x,y):
        return self.casillas[(x,y)] == ''
    def hay_victoria(self):


print