# Los alumnos de un curso se han dividido en dos 
# grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un 
# nombre anterior a la M y los hombres con un nombre 
# posterior a la N y el grupo B por el resto.
# Escribir un programa que pregunte al usuario su nombre y sexo,
# y muestre por pantalla el grupo que le corresponde.

def grupos():
    nombre = input('Ingresa tu nombre: ')
    genero = input('Cual es tu genero?(H o M): ')
    
    if(genero.lower() == 'm' and nombre.lower() < 'm'):
        a = 'Perteneces al grupo A'
    elif(genero.lower() == 'h' and nombre.lower() > 'm'):
        a = 'perteneces al grupo A'
    else:
        a = 'Perteneces al grupo B'
        
    return a
        
        
print(grupos())