# Escribir un programa que pida al usuario un número entero y
# muestre por pantalla si es par o impar.

def par():
    n1 = int(input('Ingrese un número entero: '))
    
    if (n1 % 2 == 0):
        a = f'{n1} es par.'
        
    else:
        a = f'{n1} es impar.'
        
    return a
    
    
print(par())


