# Ejercicio 3
# 
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
# nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
# mensaje En <asignatura> has sacado <nota> donde <asignatura> es
# cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
# notas introducidas por el usuario.

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for a in asignaturas:
    nota = float(input(f"Introduzca la nota que ha sacado en {a}: "))
    notas.append(nota)  # Con append se guarda dentro del array vacio cada nota sin borrar la anterior
    # print(notas) Asi vemos como se actualiza el array
 
for i in range(len(asignaturas)):  # Con un bucle que recorra hasta el ultimo valor del array sacamos cada valor que recorre en i
    print(f"En {asignaturas[i]} sacaste {notas[i]}")