class Libro:
    def __init__(self, titulo, autor, editorial, nro_paginas) -> None:
        self.titulo = titulo
        self.autor = autor
        self.editotial = editorial
        self.nro_paginas = nro_paginas

    def __str__(self) -> str:
        return f'El Libro {self.titulo} escrito por {self.autor} y publicado por {self.editotial} tiene {self.nro_paginas} páginas'
    
    def __eq__(self, otro) -> bool:
        return self.titulo == otro.titulo and self.autor == otro.autor
    
    def __add__(self, otro):
        if isinstance(otro,Libro):
            nuevo_titulo = self.titulo
            nuevo_autor = self.autor
            nuevo_editorial = self.editotial
            nuevo_nro_paginas = self.nro_paginas + otro.nro_paginas

            nuevo_libro = Libro(nuevo_titulo, nuevo_autor, nuevo_editorial, nuevo_nro_paginas)
            return nuevo_libro
        else:
            raise ValueError("La concatenacion solo esta permitida entre el objeto Libro")

libro1 = Libro("Python for beginners", "Gabriel Villacis", "Planeta", 500)
libro2 = Libro("Ultimate Python", "Josue Flores", "De Bolsillo", 600)

print(libro1)
print(libro2)

print('Son iguales Libro1 y Libro2:', libro1 == libro2 )

libro_concatenado = libro1 + libro2
print(libro_concatenado)