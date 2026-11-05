# Ejercicio 10
# 
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.
#
#   ● Ingredientes vegetarianos: Pimiento y tofu.
#   ● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
# en función de su respuesta le muestre un menú con los ingredientes disponibles
# para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
# tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
# pizza elegida es vegetariana o no y todos los ingredientes que lleva.

base = "Mozarella, tomate"

pregunta = input("¡Bienvenido a Bella Napoli! ¿Quieres una pizza vegetariana, o no vegetariana?: ")

if pregunta == "vegetariana":
    ingrediente = input("Elige un ingrediente de los siguientes: pimiento, tofu. ")
    breakpoint
elif pregunta == "no vegetariana":
    ingrediente = input("Elige un ingrediente de los siguientes: peperoni, jamón, salmón. ")
    breakpoint
# Uso breakpoint para que no se siga ejecutando el if o el elif para ahorrarme repetir el print 2 veces y dejar el código más limpio

print(f"La pizza es {pregunta} y lleva: {base} y {ingrediente}.")