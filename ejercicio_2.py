# Escribir un programa que pregunte el nombre del usuario
# en la consola y después de que el usuario lo
# introduzca muestre por pantalla la cadena ¡Hola <nombre>!, 
# donde <nombre> es el nombre que el usuario haya introducido.

def escribir_nombre():
 #esta funcion pide al usuario que ingrese un nombre y retorna la cadena 'Hola <nombre>'
  nombre = input('Como es tu nombre? ')
  cadena = f'Hola {nombre}!'
  return cadena

print(escribir_nombre())

