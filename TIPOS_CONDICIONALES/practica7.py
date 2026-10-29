# Ejercicio 7
# 
# Los tramos impositivos para la declaración de la renta en un determinado país son
# los siguientes:
# 
#       Renta                 Tipo impositivo
# 
# Menos de 10000€                    5%
# Entre 10000€ y 20000€             15%
# Entre 20000€ y 35000€             20%
# Entre 35000€ y 60000€             30%
# Más de 60000€                     45%
#
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla
# el tipo impositivo que le corresponde.

renta = float(input("Introduzca su renta anual: "))

if renta < 10000:
    resultado = f"Su tipo impositivo corresponde al 5%, por lo que {renta} se le queda en {renta * 0.95}"
else:
    if renta < 20000:
        resultado = f"Su tipo impositivo corresponde al 15%, por lo que {renta} se le queda en {renta * 0.85}"
    else:
        if renta < 35000:
            resultado = f"Su tipo impositivo corresponde al 20%, por lo que {renta} se le queda en {renta * 0.80}"
        else:
            if renta < 60000:
                resultado = f"Su tipo impositivo corresponde al 30%, por lo que {renta} se le queda en {renta * 0.70}"
            else:
                resultado = f"Su tipo impositivo corresponde al 45%, por lo que {renta} se le queda en {renta * 0.55}" 

print(resultado)