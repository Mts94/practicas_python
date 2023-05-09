#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la 
# contraseña hasta que introduzca
# la contraseña correcta.

def clave():
    pasw = 'contraseña'
    
    password = input('Escriba la clave: ')
    while (password != pasw):
        print('Clave incorrecta.')
        password = input('Escriba nuevamente la clave: ')
    
    if pasw == password:
        print('Contraseña correcta,puede ingresar')
        
        
    return pasw
        
clave()