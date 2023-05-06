# La pizzería Bella Napoli ofrece pizzas vegetarianas y
# no vegetarianas a sus clientes. Los ingredientes para
# cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza
# vegetariana o no, y en función de su respuesta le muestre un menú
# con los ingredientes disponibles para que elija. Solo se puede eligir
# un ingrediente además de la mozzarella y el tomate que están en todas
# la pizzas. Al final se debe mostrar por pantalla si
# la pizza elegida es vegetariana
# o no y todos los ingredientes que lleva.

def pizza():
    pizza1 = 'Vegetariana'
    pizza2 = 'No vegetariana'

    select = input('Que pizza desea pedir?(Vegetariana o no vegetariana): ')

    if (select.lower() == pizza1.lower()):

        ingredientes = input('Selecciona uno de estos ingredientes (Pimiento o tofu): ')
        if (ingredientes.lower() == 'pimiento'):
            a = f'Elegiste {pizza1}, sus ingredientes son mozzarella,tomate y {ingredientes}'
        elif (ingredientes.lower() == 'tofu'):
            a = f'Elegiste {pizza1}, sus ingredientes son mozzarella,tomate y {ingredientes}'
        else:
            a = 'No elegiste un ingrediente'
            

        if (select.lower() == pizza2.lower()):

            ingredientes = input(
            'Selecciona uno de estos ingredientes (Peperoni, jamon o salmon): ')
            if (ingredientes.lower() == 'peperoni'):
                a = f'Elegiste {pizza2}, sus ingredientes son mozzarella,tomate y {ingredientes}'
            elif (ingredientes.lower() == 'jamon'):
                a = f'Elegiste {pizza2}, sus ingredientes son mozzarella,tomate y {ingredientes}'
            elif (ingredientes.lower() == 'salmon'):
                a = f'Elegiste {pizza2}, sus ingredientes son mozzarella,tomate y {ingredientes}'
            else:
                a = 'No elegiste un ingrediente'

        return a


print(pizza())
