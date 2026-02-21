##PARADIGMA PROCEDURAL


##Usamos funciones para organizar el código

# PARADIGMA PROCEDURAL

def registrar_entrada(lista, placa):
    # Agrega un vehículo a la lista
    lista.append(placa)

def registrar_salida(lista, placa):
    # Elimina vehículo si existe
    if placa in lista:
        lista.remove(placa)

vehiculos = []

registrar_entrada(vehiculos, "AAA111")
registrar_entrada(vehiculos, "BBB222")

print("Vehículos:", vehiculos)

registrar_salida(vehiculos, "AAA111")

print("Después salida:", vehiculos)