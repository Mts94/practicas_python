# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que
# pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores 
# beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no 
# valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los 
# niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de

# 2.400€ multiplicada por la puntuación del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel
# de rendimiento, así como la cantidad de dinero que recibirá el usuario.

def evaluacion():
    resultado = float(input('Cual fue tu resultado obtenido: '))
    total_money = resultado * 2400
    if(resultado == 0.4):
        a = f'Tu resultado es aceptable,obtendras un bono de ${total_money:.2f}'
    elif(resultado >= 0.6):
        a = f'Tu resultado es meritorio , obtendras un bono de ${total_money:.2f}'
    elif(resultado == 0.0):
        a = 'Tu resultado es inaceptable.'
    else:
        a = 'No es un resultado valido'
    return a

print(evaluacion())

 