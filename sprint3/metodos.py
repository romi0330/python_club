from datetime import date

class profesor:
    def __init__(self, nombre: str, apellido: str):
        self.__nombre = nombre
        self.__apellido = apellido

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre

    def get_apellido(self):
        return self.__apellido
    
    def set__apellido(self, nuevo_apellido: str):
        self.__apellido = nuevo_apellido

    def __str__(self) -> str:
        return f'profesor -> (nombre: {self.__nombre}, apellido: {self.__apellido})'
    
class estudiante:
    def __init__(self, ID: int, nombre: str, apellido: str, año: date):
        self.__ID =ID
        self.__nombre = nombre
        self.__apellido = apellido
        self.__año = año

    def get_ID(self):
        return self.__ID
    
    def set_ID(self, nuevo_ID: int):
        self.ID = nuevo_ID

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre: str):
        self.nombre = nuevo_nombre

    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self, nuevo_apellido: str):
        self.apellido = nuevo_apellido

    def get_año(self):
        return self.__año
    
    def set_año(self, nuevo_año: date):
        self.año = nuevo_año

    def __str__(self) -> str:
        return f'estudiante -> (ID: {self.__ID},nombre: {self.__nombre}, apellido: {self.__apellido}, año: {self.__año})'

class curso:
    def __init__(self,codigo:int,nombre:str,profesor:profesor) -> None:
        self.__codigo = codigo
        self.__nombre = nombre
        self.__profesor = profesor
        self.__estudiantes = []

    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self, nuevo_codigo: int):
        self.codigo = nuevo_codigo

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre: str):
        self.nombre = nuevo_nombre


    def agregar_estudiantes(self, estudiante: estudiante):
        self.__estudiantes.append(estudiante)


profe1 = profesor("Gabriel", "Villacis")
print(profe1)
profe1.set_nombre("Andres")
print(profe1)
estu1 = estudiante(1,"Romina", "Villavicencio", date(2003,10,30))
print(estu1)
curso1 = curso(1,"Bootcamp Python", profe1)
curso1.agregar_estudiantes(estu1)