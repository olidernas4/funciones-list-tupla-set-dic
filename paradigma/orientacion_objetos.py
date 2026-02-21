##PARADIGMA ORIENTADO A OBJETOS (OOP)

##Modelamos el mundo real

# PARADIGMA OOP

class Vehiculo:
    # Constructor
    def __init__(self, placa):
        self.placa = placa   # Guardamos placa

    def mostrar(self):
        # Método para mostrar placa
        print("Placa:", self.placa)

# Crear objeto
v1 = Vehiculo("ABC123")
v1.mostrar()
##Característica: objetos y clases