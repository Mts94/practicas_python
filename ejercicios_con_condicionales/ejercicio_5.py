# Para tributar un determinado impuesto se debe ser mayor de 16 años
# y tener unos ingresos iguales o superiores a 1000 € mensuales.
# Escribir un programa que pregunte al usuario su edad y
# sus ingresos mensuales y muestre por pantalla
# si el usuario tiene que tributar o no.

def impuesto():
    edad = int(input('Ingrese su edad: '))
    ingreso = float(input('Cual es tu ingreso mensual?: '))
    
    if (edad > 16 and ingreso > 1000):
        a = 'Usted debe abonar el impuesto'
    else:
        a = 'Usted no debe abonar el impuesto'
        
    return a

print(impuesto())
        