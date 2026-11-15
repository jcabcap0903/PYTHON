# Ejercicio 13
# 
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
# que el usuario escriba “salir” que terminará.

ent = None

while ent != "salir":     # Se ejecuta lo de dentro del while hasta que ent no sea igual a salir
    ent = input("Escribe algo: ")
    if ent != "salir":     # Escribimos un if para que no muestre el eco tambien al poner salir, pero si no se pone también funciona pero repite salir y sale
        print(ent)
