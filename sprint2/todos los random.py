# random: https://docs.python.org/3/library/random.html

#%%
# importando módulo random
import random
import string

"""
    random()
    Obtener un número flotante aleatorio entre 0.0 y 1.0 (0 incluido y 1 no incluido)
"""
print(random.random())


#%%
"""
    uniform(a, b)
    Obtener un número flotante aleatorio entre los dos números especificados a y b, ambos incluidos
"""
print(random.uniform(5, 50))


#%%
"""
    randint(a, b)
    Obtener un número entero aleatorio entre los dos números especificados a y b, ambos incluidos    
"""
print(random.randint(10, 12))


#%%
"""
    random.randrange(start, stop, step) 
    Obtener un elemento seleccionado aleatoriamente del rango especificado.

    start: Opcional. Un número entero que especifica en qué posición comenzar. Predeterminado: 0
    stop: Requerido. Un número entero que especifica en qué posición terminar
    step: Opcional. Un número entero que especifica el incremento. Predeterminado: 1
"""
print(random.randrange(1, 50))
print(random.randrange(0, 20, 2))
print(random.randrange(-500, 500, 5))

#%%
"""
    random.choice(sequence)
    Obtener un elemento aleatorio desde una secuencia (array). Si la secuencia está vacía, provoca IndexError
    La secuencia puede ser una lista, una tupla, una cadena de caracteres, un rango de números, etc.    
"""
print(random.choice([1,2,3,4,5,6,10]))
print(random.choice([10,20,30,40,50,60,70,80,90,100]))
print(random.choice('Hola-Mundo'))
print(random.choice(['David', 'Maria', 'Daniel', 'Hector', 'Joaquin']))


#%%
"""
    random.choices(sequence, k)
    Obtener una lista de k elementos aleatorios desde una secuencia (array). Si la secuencia está vacía, provoca IndexError    
    La secuencia puede ser una lista, una tupla, una cadena de caracteres, un rango de números, etc.
"""
print(random.choices([1,2,3,4,5,6,10], k=2))
print(random.choices([10,20,30,40,50,60,70,80,90,100], k=3))
print(random.choices('Hola-Mundo', k=2))
print(random.choices(['David', 'Maria', 'Daniel', 'Hector', 'Joaquin'], k=1))

# Ejemplo: Generación de contraseña aleatoria
print("".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10)))


"""
    random.shuffle(sequence)
    Reordenar aleatoriamente los elementos de una secuencia mutable.
   
    La secuencia puede ser una lista, una cadena de caracteres, un rango de números, etc. 
"""
nombres = ['Gabriel', 'Antonio', 'David', 'Hugo', 'Jessica', 'Carla']
random.shuffle(nombres)
print(nombres)

# %%
