# Ejercicio 3
# 
# Escribir un programa que pida al usuario dos números y muestre por pantalla su
# división. Si el divisor es cero el programa debe mostrar un error.

num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))
if num2 == 0:
    print("ERROR")
else:
    division = num1 / num2
    print(f"El resultado de la division entre {num1} y {num2} es: {division}")