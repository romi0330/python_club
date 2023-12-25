"""Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no"""
while True:
    año = int(input("Ingrese un año: \n"))
    
    if año%400 ==0:
        print("BISIESTO")
    elif año%4 == 0 and año%100 != 0:
        print("BISIESTO")
    else:
        print("NO ES BISIESTO")
    
    continuar= input('¿Desea hacer otro calculo? si/no \n')
    if continuar == 'no':
       break
