# Escribir un programa que pregunte al usuario su edad 
# y muestre por pantalla si es mayor de edad o no.

def edad():
    edad = int(input('Ingrese su edad: '))
    
    if edad >= 18:
        a = 'Es mayor de edad'
        
    else:
        a = 'Es menor de edad'
        
    return a
        

print(edad())