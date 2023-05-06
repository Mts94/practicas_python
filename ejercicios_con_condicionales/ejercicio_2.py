# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


contrasenia = input('Cree su clave: ')


def valida_clave(contrasenia):
    contrasenia = contrasenia.lower()
    clave = input('Bienvenido,ingrese su clave: ')
    clave = clave.lower()
    
    if(clave == contrasenia):
        a = 'Las contraseñas coinciden'
      
    else:
        a = 'Las contraseñas no coinciden'
          
    return a
    

print(valida_clave(contrasenia))