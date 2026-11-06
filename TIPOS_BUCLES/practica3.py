# Ejercicio 3
# 
# Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla todos los números impares desde 1 hasta ese número separados por
# comas.

num = int(input("Introduzca un numero entero positivo: "))

for n in range(1, num + 1, 2):
    print(n, end=", ")