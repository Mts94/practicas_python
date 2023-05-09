# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el 
# capital obtenido en la inversión
# cada año que dura la inversión.

def inversion():
    cantidad = float(input('Ingrese la cantidad a invertir: '))
    interes = float(input('Cual es el interés anual?: '))
    interes = interes / 100
    anios = int(input('Ingrese la cantidad de años a invertir: '))
    capital_obtenido = cantidad
    
    for i in range(1,anios):
        capital_obtenido += capital_obtenido * interes
        capital_obtenido *= 1 +  interes
        
       
        print("%.2f" % capital_obtenido)
        
        
            
    return capital_obtenido


inversion() 
        