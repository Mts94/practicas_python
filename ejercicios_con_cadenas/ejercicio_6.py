# Escribir un programa que pida al usuario que introduzca 
# una frase en la consola y una vocal, y después muestre por pantalla la misma 
# frase pero con la vocal introducida en mayúscula.

def frase():
    a = input('Ingrese una frase: ')
    b = input('Ingrese una vocal(a-u): ')
    
    c = a.replace(b, b.upper())
    
    return c


