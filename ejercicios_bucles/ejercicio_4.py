# Escribir un programa que pida al usuario un
# número entero positivo y muestre por pantalla la cuenta atrás desde ese número
# hasta cero separados por comas.

def cuenta_atras():
    num = int(input('Ingrese un número entero: '))
    
    for i in range(1, num+1):
        print(num - i, end=', ')
        
    return num


cuenta_atras()