# Escribir un programa que pregunte al usuario por el número de horas trabajadas
# y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.

def horas_trabajo():
    h = input('Hola,cuantas horas trabajaste hoy? ')
    c = input('Cuantos es el pago por hora trabajada? ')
    f = float(h)*float(c)
    cf = f'El pago que le corresponde por su trabajo es {f}'
    return cf

print(horas_trabajo())