# Escribir un programa que pregunte al usuario la fecha 
# de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
# el día, el mes y el año. Adaptar el programa anterior para que 
# también funcione cuando el día o el mes se introduzcan con un solo carácter.

def fecha_de_nac():
    fecha = input('Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ')
    salida = 'Dia', fecha[:2], 'mes' ,fecha[3:5], 'año', fecha[6:]
    return salida


