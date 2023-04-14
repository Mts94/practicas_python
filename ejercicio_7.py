# Escribir un programa que pida al usuario dos números enteros y 
# muestre por pantalla la <n> entre <m> da un cociente <c>
# y un resto <r> donde <n> y <m> son los números introducidos
# por el usuario, y <c> y <r> son 
# el cociente y el resto de la división entera respectivamente.


def coc_res():
    n = float(input('ingrese un número: '))
    m = float(input('Ingrese un segundo número: '))
    cociente = n / m
    resto = n % m
    res = f'El cociente de la division es {cociente} y el resto de la misma es {resto}'
    return res

print(coc_res())