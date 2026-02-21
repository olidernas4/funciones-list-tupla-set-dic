##PARADIGMA FUNCIONAL

##Usamos funciones puras (sin cambiar datos originales)

# PARADIGMA FUNCIONAL

def calcular_total(horas):
    # No cambia nada externo
    return horas * 2000

total = calcular_total(3)
print("Total a pagar:", total)