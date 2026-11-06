# Ejercicio 7
# 
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for a in range(1, 10 + 1):
    for b in range(1, 10 + 1):
        print(f"{a} * {b} = {a * b}")