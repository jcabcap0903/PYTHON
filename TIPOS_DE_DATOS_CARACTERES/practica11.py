# Ejercicio 11
#
# Escribir un programa que pregunte el nombre el un producto, su precio y un número
# de unidades y muestre por pantalla una cadena con el nombre del producto seguido
# de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
# tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

nombre = input("Introduzca el nombre del producto: ")
precio = float(input("Introduzca el precio del producto: "))
unidades = int(input("Introduzca el número de unidades del producto: "))
total = precio * unidades
print(f"{nombre}: {precio:09.2f}€ x {unidades:03d} unidades = {total:011.2f}€")