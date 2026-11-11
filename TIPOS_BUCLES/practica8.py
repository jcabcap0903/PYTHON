# Ejercicio 8
# 
# Escribir un programa que pida al usuario un número entero y muestre por pantalla
# un triángulo rectángulo como el de más abajo.

num = int(input("Introduzca un número entero: "))

for s in range(1, num + 1, 2):
    for i in range(s, 0, -2):
        print(i, end=" ")
    print()