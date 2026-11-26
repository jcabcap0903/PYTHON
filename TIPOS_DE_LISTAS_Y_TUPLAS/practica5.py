# Ejercicio 5
# 
# Escribir un programa que almacene en una lista los números del 1 al 10 y los
# muestre por pantalla en orden inverso separados por comas.

nums = []

for num in range(0, 10):
    nums.append(num + 1)

nums.reverse()

for n in nums:
    print(n, end=", ")