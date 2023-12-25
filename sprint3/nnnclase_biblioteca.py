from typing import Any
from typing import List

class Libro:
    def __init__(self, titulo : str, autor : str, genero : str):  #Type Hints
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
    
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, nuevo_titulo : str):
        self.__titulo = nuevo_titulo

    def get_autor(self):
        return self.__autor
    
    def set_autor(self,nuevo_autor : str):
        self.__autor = nuevo_autor

    def get_genero(self):
        return self.__genero
    
    def set_genero(self,nuevo_genero : str):
        self.__genero = nuevo_genero

    
    def __str__(self) -> str:
        return f'Libro -> (titulo : {self.__titulo}, autor: {self.__autor}, genero: {self.__genero})'
    

class Biblioteca:
    def __init__(self):  #Type Hints
        self.__libros = []

    def agregar_libros(self, libros):
        self.__libros.append(libros)

    def eliminar_libro(self, libros):
        self.__libros.remove(libros)
    
    def mostrar_libros(self):
        print(self.__libros)