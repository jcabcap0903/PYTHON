inv = int(input("¿Cuánto quieres invertir?: "))
ian = float(input("Introduzca el interés anual (%): "))
ano = int(input("Introduzca el número de años: "))

capital = inv * (1 + ian / 100) ** ano
capital = round(capital, 2)

print(f"El capital obtenido tras {ano} años es: {capital}")