
class Vehiculo:
    def __init__(self,marca, modelo, color, placa) -> None:
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.placa = placa

    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo


class Carro(Vehiculo):
    def __init__(self, marca, modelo, color, placa, nro_puertas) -> None:
        super().__init__(marca, modelo, color, placa)
        self.nro_puertas = nro_puertas
 

class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, placa, tipo_moto) -> None:
        super().__init__(marca, modelo, color, placa)
        self.tipo_moto = tipo_moto

moto1 = Moto("KTM","Enduro 5000","Rojo", "YF589","Tiaja")
print (moto1.get_marca())
print (moto1.get_modelo())

