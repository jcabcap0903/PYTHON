kg = float(input("Introduzca su peso (kg): "))
m = float(input("Introduzca a continuacion su estatura (m) *use puntos*: "))

imc = kg / (m * m)
imc = round(imc, 2)

print(f"Su índice de masa corporal es {imc}")