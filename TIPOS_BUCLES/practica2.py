# Ejercicio 2
# 
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
# los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Introduzca su edad: "))

for e in range(1, edad + 1): # empieza en 1, llega hasta edad + 1 para que no acabe en el numero anterior
    print(e)