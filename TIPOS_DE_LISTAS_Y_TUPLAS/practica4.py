# Ejercicio 4
# 
# Escribir un programa que pregunte al usuario los números ganadores de la lotería
# primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
# a mayor.

nums = []

for num in range(0, 6):
    num = int(input("Introduzca los números ganadores de la primitiva (6 entre 1 y 49): "))
    nums.append(num)

nums.sort()

print(nums)