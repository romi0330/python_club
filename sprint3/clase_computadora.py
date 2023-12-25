
class Computadora:
    #Constructor
    def __init__(self, p_procesador, p_ram, p_conectividad, p_tipo, p_esta_pagada, p_precio):
        self.procesador = p_procesador
        self.ram = p_ram
        self.tipo = p_tipo
        self.conectividad = p_conectividad
        self.esta_pagada = p_esta_pagada
        self.precio = p_precio


    #Atributos
    """  procesador = 'Amd Ryzen 5600x'
    ram = '32GB'
    conectividad = 'wireless'
    esta_pagada = 'True'
    precio = 1500 """

# objetos (Son los que estan en tiempo de ejecución)
computadora1 = Computadora('Ryzen 5600x','32GB','desktop','w',True,1500)
print(computadora1.procesador)

computadora2 = Computadora('Core i9','64GB','desktop','w',False,1600)
print(computadora2.procesador)
