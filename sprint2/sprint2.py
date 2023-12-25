import re
import csv
lista = []

def agregar():
    while True:
        nombre = str(input("Ingrese el nombre del estudiante sin carácteres especiales: \t"))
        validar = re.findall(r"[a-zA-Z\s]", nombre)
        if validar and len(validar) == len(nombre):
            break
        else:
            print("Error. El nombre solo puede contener letras")

    edad = int(input("Ingrese la edad del estudiante: \t"))
    curso = int(input("Ingrese el código del curso del estudiante (Ej. 125): \t"))

    estudiante = {"nombre": nombre, "edad": edad, "curso": curso}
    lista.append(estudiante)


def buscar():
    buscar_estudiante = str(input("Ingrese el nombre del estudiante que desea buscar: \t"))

    for estudiante in lista:
        if estudiante["nombre"] == buscar_estudiante:
            print(f"Estudiante {estudiante["nombre"]} encontrado, con edad de {estudiante["edad"]} y curso {estudiante["curso"]}")
            break
        else:
            print("Estudiante no encontrado")


def eliminar():
    eliminar_estudiante = str(input("Ingrese el nombre del estudiante que desea despedir: \t"))
    eliminados = []
    for estudiante in lista:
        if estudiante["nombre"] == eliminar_estudiante:
            eliminados.append(estudiante)
            lista.remove(estudiante)
            print("Estudiante eliminado con éxito")
        else:
             print("No se econtró al estudiante")


def exportar(lista, estudiantes):
    ordenar = sorted(lista, key=lambda est:est["nombre"])
    try:
        with open(estudiantes, 'w', newline='', encoding='UTF-8') as archivo:
            campos = ['nombre', 'edad', 'curso']
            escritor = csv.DictWriter(archivo,fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(ordenar)
            print(f"Los datos se han guardado en {estudiantes}")
    except IOError:
        print(f"No se pudo escribir en el archivo {estudiantes}")
    

def contar():
    buscar_curso = int(input("Ingrese el curso para ver cuantos estudiantes hay en el: \t"))
    contador = 0
    for curso in lista:
        if curso["curso"] == buscar_curso:
            contador += 1 
    print(f"Hay {contador} estudiantes en el curso {buscar_curso}")


while True:
    print( "\n \tM E N U")
    print("1. Agregar Estudiante")
    print("2. Buscar Estudiante")
    print("3. Eliminar Estudiante")
    print("4. Exportar a CSV")
    print("5. Contar estudiantes de un curso")
    print("6. Salir")
    menu = input("\nIngrese su opción:\t")

    if menu == "1":
        agregar()
    elif menu == "2":
        buscar()
    elif menu == "3":
        eliminar()
    elif menu == "4":
        exportar(lista,'estudiante.csv')
    elif menu == "5":
        contar()
    elif menu == "6":
        break
    else:
        print("Error, ingrese un número de 1-6")
    