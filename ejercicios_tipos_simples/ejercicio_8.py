# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años,
# y muestre por pantalla el capital obtenido en la inversión.

def invertir():
    cantidad = float(input('Cuanto es la cantidad que desea invertir?: '))
    interes = float(input('Cuanto es el interes interanual?: '))
    anios = float(input('Por cuantos años vas a invertir: '))
    
    capital = (cantidad * interes) / 100 
    total = capital * anios
    capital_total = f'El total de capital que vas a obtener es {total+cantidad}'    
    return capital_total

print(invertir())