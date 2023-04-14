# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece 
# el 4% de interés al año. Estos ahorros debido a intereses, que no se 
# cobran hasta finales de año, se te añaden al balance final de tu cuenta 
# de ahorros. Escribir un programa que comience leyendo la cantidad de dinero
# depositada en la cuenta de ahorros, introducida por el usuario.
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer,
# segundo y tercer años. Redondear cada cantidad a dos decimales.

def interes():
    a = float(input('Ingrese la cantidad de dindero que desea invertir: '))
    primer = (a * 0.04) + a
    
    segundo = (primer * 0.04) + primer
    
    tercero = (segundo * 0.04) + segundo

    
    total = f'El primer año obtendrias ${primer:.2f}, el segundo año obtendrias ${segundo:.2f} y el tercer año ${tercero:.2f}'
    return total


print(interes())