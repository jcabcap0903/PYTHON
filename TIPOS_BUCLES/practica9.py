# Ejercicio 9
# 
# Escribir un programa que almacene la cadena de caracteres contraseña en una
# variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
# correcta

pin = None # Se declara vacia primero para poder usarla en el while, ya que le damos valor dentro del mismo y no puede comprobar que exista antes
pinreal = "Macarrones123"

while pin != pinreal:  # Mientras que lo que meta en la variable pin no sea pinreal, no sale del while y vuelve a preguntar hasta introducirla bien
    pin = input("Introduzca la contraseña: ")