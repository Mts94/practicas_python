# Escribir un programa que lea un entero positivo, n
# , introducido por el usuario y después muestre en 
# pantalla la suma de todos los enteros desde 1 hasta n
# . La suma de los n
#  primeros enteros positivos puede ser calculada de la siguiente forma:


def sumas():
    n =int(input('Indique un número entero: '))
    suma = n * (n + 1) /2
    
    return suma

print(sumas())