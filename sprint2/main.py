import csv

# Función leer_csv => retornar el contenido del archivo en una lista de diccionarios
def leer_csv(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='UTF-8') as arhivo:
            lector = csv.DictReader(arhivo)
            return list(lector)
    except FileNotFoundError:
        print(f'El archivo {nombre_archivo} no existe')
        return []

# Función filtrar_datos => Filtrar la lista de estudiantes y retorna solo aquellos estudiantes con un valor de puntuacion especifico (>=puntuacion)
""" def filtrar_datos(lista_a_filtrar, puntuacion):
    lista_temp = []
    for d in lista_a_filtrar:
        if(int(d.get('puntuacion'))>=puntuacion):
            lista_temp.append(d)
        
    return lista_temp
 """
 
def filtrar_datos(lista_a_filtrar, puntuacion):
    return [e for e in lista_a_filtrar if int(e.get('puntuacion'))>=puntuacion]


# Función guardar_csv => Guardar la lista de estudiantes filtrada en un nuevo archivo
def guardar_csv(lista_a_guardar, nombre_archivo):
    try:
        with open(nombre_archivo, 'w', newline='', encoding='UTF-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['nombre', 'edad', 'puntuacion', 'asistencia'])
            escritor.writeheader()
            escritor.writerows(lista_a_guardar)
        print(f'Los datos filtrados se han guardado en {nombre_archivo} correctamente')
    except IOError:
        print(f'No se pudo escribir en el archivo {nombre_archivo}')
        

# Programa principal
lista = leer_csv('alumnos.csv')
lista_filtrada = filtrar_datos(lista, 80)
guardar_csv(lista_filtrada, 'resultados_filtrados.csv')