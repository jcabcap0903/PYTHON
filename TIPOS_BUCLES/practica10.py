# Ejercicio 10
#
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si
# es un número primo o no.

num = int(input("Introduzca un número entero: "))

primo = True   # Declaramos la variable primo para ir dandole valor. Empezamos Dandole True de base

if num < 2:     # Antes del 2 no hay ningun primo, por lo que False
    primo = False
else:           # Si es 2 o mayor comparamos otra cosa
    for i in range(2, num):        # Contamos todos los números desde el primero (2) hasta el último número antes del mismo que queremos comprobar si es primo
        if num % i == 0:          # Si el numero a comparar da con el número del bucle resto 0 no puede ser primo porque se podria dividir entre más
            primo = False
            break      # Como mínimo 1 número al dividir con él da resto 0, no comparamos más números innecesariamente y sale del bucle

if primo == True:         # Si sobrevive a todo no se le cambia el valor a False y sería primo, es decir, solo se puede dividir entre 1 y el mismo y no daría decimal
    print("Es primo")
else:
    print("No es primo")