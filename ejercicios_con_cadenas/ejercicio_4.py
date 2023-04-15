# Los teléfonos de una empresa tienen el siguiente formato 
# prefijo-número-extension donde el prefijo es el código del país +34,
# y la extensión tiene dos dígitos 
# (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un 
# número de teléfono con este formato y muestre por 
# pantalla el número de teléfono
# sin el prefijo y la extensión.

def telefono():
    #se pide a usuario ingresar un número telefónico con un formate determinado
    telefono = input('Ingrese un número de teléfono con el formato +xx-xxxxxxxxx-xx: ')
    #retorna un str la notación [4:-3] indica desde que posición de la cadena hasta que posición debe mostrar por pantallla
    salida = f'El número telefónico es  {telefono[4:-3]}'
    return salida


print(telefono())