# Una panadería vende barras de pan a 3.49€ cada una.
# El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de 
# barras vendidas que no son del día. Después el programa
# debe mostrar el precio habitual de una barra de pan,
# el descuento que se le hace por no ser fresca
# y el coste final total.

def pan():
    vendidas = int(input('Cuantas barras de pan que no son del dia se vendieron hoy?: '))
    costo_original = 3.49
    costo_con_descuento = 3.49 * 0.6
    costo_final = costo_con_descuento * vendidas
    
    mostrar = f'''El precio habitual del pam es ${costo_original}, al no ser del dia tiene un descuento de 60%
    ${costo_con_descuento:.2f},el costo final es de ${costo_final:.2f}
    '''
    return mostrar

print(pan())