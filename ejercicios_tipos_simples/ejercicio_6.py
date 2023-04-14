# Escribir un programa que pida al usuario su peso (en kg) y 
# estatura (en metros), calcule el índice de masa corporal y
# lo almacene en una variable, y muestre por pantalla la frase
# Tu índice de masa corporal es <imc> donde <imc> es el índice
# de masa corporal calculado redondeado con dos decimales.

def imc():
    peso = float(input('Ingrese su peso corporal actual en kg: '))
    altura = float(input('Ingrese su altura en mts: '))
    
    imc = peso / altura**2
    
    res = f'Su indice de masa corporal es {imc:0.2f}'
    return res

print(imc())
