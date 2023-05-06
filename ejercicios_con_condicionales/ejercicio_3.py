# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

def division():
    n1 = int(input('Ingrese el primer número: '))
    n2 = int(input('Ingrese un divisor: '))
    
    if(n2 == 0):
        a = 'Error!,el divisor no puede ser 0.'
        return a
    else:
        a  = n1/n2
        
    return a
    
    
print(division())