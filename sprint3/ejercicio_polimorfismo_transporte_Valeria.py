from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def calcular_costo(self):
        pass

class Autobus(Transporte):
    def __init__(self, distancia, pasajeros):
        self.distancia = distancia
        self.pasajeros = pasajeros

    def calcular_costo(self):
        costo_por_km = 0.1
        costo_total = self.distancia * costo_por_km + (self.pasajeros * 0.5)
        return costo_total

class Avion(Transporte):
    def __init__(self, distancia, pasajeros, tarifa_aerea):
        self.distancia = distancia
        self.pasajeros = pasajeros
        self.tarifa_aerea = tarifa_aerea

    def calcular_costo(self):
        costo_por_km = 0.5
        costo_total = self.distancia * costo_por_km + (self.pasajeros * 1.5 * self.tarifa_aerea)
        return costo_total

def mostrar_costos(transportes):
    for transporte in transportes:
        print(f"Costo de transporte: {transporte.calcular_costo()}")


transportes = [
    Autobus(distancia=200, pasajeros=30),
    Avion(distancia=1000, pasajeros=150, tarifa_aerea=2.0),
    Autobus(distancia=150, pasajeros=20),
    Avion(distancia=800, pasajeros=100, tarifa_aerea=1.5)
]

mostrar_costos(transportes)
