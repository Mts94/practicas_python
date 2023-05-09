# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tablas():
    num = int(input('Ingrese un número entero: '))
    
    for i in range(1,12+1):
        print(f'{num}*{i} es igual a: {i*num}' )
        
        
        
    return num

tablas()

