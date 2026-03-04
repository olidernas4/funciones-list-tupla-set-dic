
## clase padre
class Carro:
    def __init__(self, marca):
        self.marca = marca
    
    def conducir(self):
        print("El carro esta conduciendo")


class CarroElectronico(Carro):

    def cargar_bateria(self):
        print("Cargando batería")

tesla=CarroElectronico("Tesla")

tesla.conducir()
tesla.cargar_bateria()



## class

class CarroGasolina:
    def mover(self):
        print("usa gasolinas")

class Carroelectronico:
    def mover(self):
        print("usa lectricidad")

vehiculos = [CarroGasolina(), Carroelectronico()]

for v in vehiculos:
    v.mover()


    
