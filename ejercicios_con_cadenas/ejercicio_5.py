# Escribir un programa que pida al usuario que introduzca una frase en la consola y
# muestre por pantalla la frase invertida.

def palabra():
    a = input('Ingrese una pabalra o frase: ')
    b = a[::-1]
    return b
  


print(palabra())