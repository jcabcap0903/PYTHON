bpas = float(input("¿Cuántas barras se han vendido que no son de día?: "))

phab = 3.49
desc = 0.60
cfin = (phab * bpas) * (1 - desc)
cfin = round(cfin, 2)

print(f"El precio habitual de una barra de pan es {phab}€")
print(f"El descuento por no ser fresca es de {desc} (60%)")
print(f"El precio final es {cfin}€")