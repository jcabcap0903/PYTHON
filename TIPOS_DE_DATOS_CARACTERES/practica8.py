# Ejercicio 8
#
# Escribir un programa que pregunte por consola el precio de un producto en euros
# con dos decimales y muestre por pantalla el número de euros y el número de
# céntimos del precio introducido.

precio = input("Introduzca el precio del producto seleccionado (€.xx): ")
preciosep = precio.split(".")
print(f"El producto seleccionado cuesta {preciosep[0]} € con {preciosep[1]} centimos")