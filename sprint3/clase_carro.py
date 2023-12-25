class Carro:
    def __init__(self, c_marca, c_modelo, c_color, c_num_chasis, c_placa):
        self.marca = c_marca
        self.modelo = c_modelo
        self.color = c_color
        self.num_chasis = c_num_chasis
        self.placa = c_placa

    def acelerar(self):
        print('Acelerando..')
    
    def frenar(self):
        print('Frenando...')


carro1 = Carro("Chevrolet","C","Rojo",2356,"Y5478")
carro2 = Carro("Nissan","A","Negro",8676,"D5478")
carro3 = Carro("Lamborgini","D","Amarillo",86796,"O5478")

carro1.acelerar()
carro2.frenar()
carro3.acelerar()
print(carro1.color)