from abc import ABC, abstractmethod

class Libro (ABC):
    def __init__(self, titulo : str, autor: str) -> None:
        self.titulo = titulo
        self.autor = autor
        
    @abstractmethod
    def calcular_precio(self) -> float:
        pass

class LibroFisico(Libro):
    VALOR_BASE = 10 
    PRECIO_POR_PAGINA = 0.1

    def __init__(self, titulo : str, autor: str, nro_paginas : int) -> None:

        super(LibroFisico, self).__init__(titulo, autor)
        self.nro_paginas = nro_paginas
    
    

    def calcular_precio(self) -> float:
        precio = self.VALOR_BASE + (self.nro_paginas * self.PRECIO_POR_PAGINA)
        return precio
    


class LibroDigital(Libro):
    VALOR_BASE = 5 
    PRECIO_POR_MEGABYTE = 0.1

    def __init__(self, titulo : str, autor: str, nro_mb : float) -> None:

        super(LibroDigital, self).__init__(titulo, autor)
        self.nro_mb = nro_mb
    

    def calcular_precio(self) -> float:
        precio = self.VALOR_BASE + (self.nro_mb * self.PRECIO_POR_MEGABYTE)
        return precio
    




libro_fisico = LibroFisico('Cien años de soledad', 'Gabriel Garcia Marquez', 250)
print(f'Precio Libro fisico:  {libro_fisico.calcular_precio()}')


libro_digital = LibroDigital("El codigo da Vinci", "Dan Brown", 2.8)
print(f'Precio Libro digital:  {libro_digital.calcular_precio()}')