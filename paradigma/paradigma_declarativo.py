##PARADIGMA DECLARATIVO
##Decimos qué queremos, no cómo

# PARADIGMA DECLARATIVO usando comprensión de listas

vehiculos = ["ABC123", "BBB222", "CCC333"]

# Queremos solo placas que empiezan por B
filtrado = [v for v in vehiculos if v.startswith("B")] # esta funcion hace el filtrado por nosotros, no le decimos cómo hacerlo, solo qué queremos

print("Filtrados:", filtrado)