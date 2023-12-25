#%% Ejercicio 1: Definir una función para determinar si un número es par o impar.

def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

valor = 5
resultado = es_par(valor)
print('El ', valor, ' es par ', resultado)

#%% Ejercicio 2: Definir una función que permita sumar dos números.

def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

print(sumar(5, 10))

# %%
