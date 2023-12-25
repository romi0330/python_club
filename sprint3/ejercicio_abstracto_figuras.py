from abc import ABC, abstractmethod
import math

class FiguraGeometrica (ABC):
    
    @abstractmethod
    def calcular_area(self):
        pass
        
class Circulo(FiguraGeometrica):

    def __init__(self, radio: float) -> None:
        self.radio = radio

    def calcular_area(self) -> float:
        area = math.pi * (self.radio ** 2)
        return area

class Rectangulo(FiguraGeometrica):
    
    def __init__(self, base: float, altura : float) -> None:
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        area = self.base * self.altura
        return area


area_c = Circulo(2.9)
print(f' El area del circulo es: {area_c.calcular_area()}')

area_r = Rectangulo(3.0 , 4.0)
print(f' El area del rectangulo es: {area_r.calcular_area()}')
