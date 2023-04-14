# Una juguetería tiene mucho éxito en dos de sus productos:
#     payasos y muñecas. Suele hacer venta por correo y 
#     la empresa de logística les cobra por peso de cada paquete
#     así que deben calcular el peso de los payasos y muñecas que 
#     saldrán en cada paquete a demanda. Cada payaso pesa 112 g 
#     y cada muñeca 75 g. Escribir un programa que lea el número de 
#     payasos y muñecas vendidos en el último pedido y calcule el peso total 
#     del paquete que será enviado.

def peso():
    pedidoP = float(input('Cuantas unidades de payasos va a querer: '))
    pedidoM = float(input('Cuantas unidades de muñecas va a querer: '))
    payaso = 112
    munieca = 75
    
    pesoP = pedidoP * payaso
    pesoM = pedidoM * munieca
    
    peso_total = pesoP + pesoM
    
    peso = f'El pedido tendra un peso total de {peso_total} gramos'
    return peso
    
print(peso())
