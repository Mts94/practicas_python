# Escribir un programa que pregunte por consola por los
# productos de una cesta de la compra, separados por comas,
# y muestre por pantalla cada uno de los productos en una línea distinta.


def productos():
  productos = input("Introduce los productos separados por comas: ")
  lista_productos = productos.split(",")

  a = "\n".join(lista_productos)
  
  b = f'Los productos de tu lista son : {a}'
  
  return b


print(productos())
  
  