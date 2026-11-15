# Ejercicio 12
# 
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
# muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Introduzca una frase: ")
letra = input("Introduzca una letra: ")

contador = 0  # declaramos el contador para poder usarlo en la comparacion

for c in frase:    # saca cada caracter de frase y los lee 1 por 1
    if c == letra:   # si el caracter actual es igual a la letra suma 1 en el contador
        contador+=1

print(f"La letra {letra} aparece {contador} veces en {frase}")