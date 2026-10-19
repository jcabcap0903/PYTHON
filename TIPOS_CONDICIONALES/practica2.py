# Ejercicio 2
#
# Escribir un programa que almacene la cadena de caracteres <contraseña> en una
# variable, pregunte al usuario por la contraseña e imprima por pantalla si la
# contraseña introducida por el usuario coincide con la guardada en la variable sin
# tener en cuenta mayúsculas y minúsculas.

contraseniaReal = "Javi123"
contraseniaInt = input("Introduzca la contraseña: ")
if contraseniaInt.lower() == contraseniaReal.lower():
    print("La contraseña es correcta, acceso concedido")
else:
    print("La contraseña es incorrecta, intentelo de nuevo")