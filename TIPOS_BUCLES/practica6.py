# Ejercicio 6
# 
# Escribir un programa que pida al usuario un número entero y muestre por pantalla
# un triángulo rectángulo como el de más abajo, de altura el número introducido

num = int(input("Introduzca un número entero: "))

for n in range(1, num):
    print("*" * n)