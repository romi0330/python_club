#%% Definir una funcion para determinar si un numero es par o impar

def es_par(num):
    if num%2 == 0:
        return True
    else:
        return False
    
valor = 5
resultado = es_par(valor)
print("¿El", valor, "es par?", resultado)


# %%  Definir una función que permita sumar dos números.

def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

print(sumar(5, 10))


# %% multilista

def multiLista(lista):
    multi = 1
    for numero in lista:
        multi = multi * numero
    return multi
    
print(multiLista([2,2.5,10]))
print(multiLista([8,2,3,-1,7]))
print(multiLista([1.5,5,50,0,-4]))

# %% voltear texto

def voltearTexto(texto):
  return texto[::-1]

texto = str(input("Ingrese un texto: "))
texto_invertido = voltearTexto(texto)
print(texto_invertido)


