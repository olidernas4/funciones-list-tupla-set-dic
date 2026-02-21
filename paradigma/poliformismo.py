##EJERCICIO 3 — POLIMORFISMO
##Mismo método, distinto comportamiento

# POLIMORFISMO

class Carro:
    def pagar(self):
        print("Tarifa carro 3000")

class Moto:
    def pagar(self):
        print("Tarifa moto 1500")

def cobrar(vehiculo):
    vehiculo.pagar()  # No importa el tipo

c = Carro()
m = Moto()

cobrar(c)
cobrar(m)