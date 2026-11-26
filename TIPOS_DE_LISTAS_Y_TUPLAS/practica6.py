# Ejercicio 6
# 
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
# nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
# aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
# usuario tiene que repetir.

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua" ]

for a in asignaturas.copy():  # Como se salta posiciones si se usa el original, hacemos una copia para que no salte puestos y aplicamos en el original
    nota = int(input(f"Introduzca la nota que ha sacado en {a}: "))
    if nota >= 5:
        asignaturas.remove(a)

print("Asignaturas que tiene que repetir:")
for a in asignaturas:
    print(a)
