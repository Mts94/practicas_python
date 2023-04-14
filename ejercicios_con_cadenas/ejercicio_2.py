# Escribir un programa que pregunte el nombre completo del usuario en la consola
# y después muestre por pantalla el nombre completo del usuario tres veces,
# una con todas las letras minúsculas, otra con todas las letras mayúsculas y
# otra solo con la primera letra del nombre y de los apellidos en mayúscula.
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.


def nombre_completo():
    nombre = input('Ingresa tu nombre completo: ')
    
    nombre_minuscula = nombre.lower()
    
    nombre_mayuscula = nombre.upper()
   
    nombres_primmay = nombre.title()
    
    nombres =f'''Este es tu nombre completo con letras minusculas {nombre_minuscula},
    este es tu nombre completo en letras mayúsculas {nombre_mayuscula} y 
    este es tu nombre completo con cada letra de inicio en mayúsculas {nombres_primmay}.
    '''
    
    return nombres


print(nombre_completo())
    
    
