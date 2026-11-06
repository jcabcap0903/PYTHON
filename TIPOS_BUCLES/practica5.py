# Ejercicio 5
# 
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
# año que dura la inversión.

invertir = int(input("Introduzca la cantidad a invertir: "))
interes = int(input("Introduzca el interés anual: "))
anios = int(input("Introduzca al número de años: "))

for i in range(1, anios + 1):
    invertir = invertir + (invertir * (interes / 100))
    print(invertir)