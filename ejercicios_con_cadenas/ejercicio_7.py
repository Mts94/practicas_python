# Escribir un programa que pregunte el correo electrónico del usuario en
# la consola y muestre por pantalla otro
# correo electrónico con el mismo nombre 
# (la parte delante de la arroba @) pero con dominio ceu.es.

def email():
    email = input('Ingrese su Email: ')
    #'''utilizam,os la funcion split() indicamos
    # entre parentesis que caracater a buscar y entre corchetes desde donde comenzara
    #en la primera que encuentre true cortara s str
    nombre = email.split('@')[0]
    
    nuevo_correo = f'{nombre}@ceu.es'
    
    return nuevo_correo

