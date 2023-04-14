# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
# imprima por pantalla en líneas distintas el nombre del 
# usuario tantas veces como el número introducido.

def nombre():
    nombre = input('Ingrese su nombre: ')
    cantidad = int(input('Cuantas veces repetimos?: '))
    
    

    for i in range(cantidad-1):
        print(nombre)
        
    return nombre
        
                    
    
    
