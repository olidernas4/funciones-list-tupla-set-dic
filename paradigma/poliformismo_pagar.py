#Ejemplo de la vida real

#Piensa en el botón "Pagar" en tu parqueadero 

#liente carro → paga 3000

#Cliente moto → paga 1500

#Cliente camión → paga 6000

#El botón se llama igual: pagar
#Pero hace cosas diferentes.


# Creamos clases diferentes

class Carro:
    def pagar(self):
        # Este método es para carros
        print("Carro paga 3000")

class Moto:
    def pagar(self):
        # Este método es para motos
        print("Moto paga 1500")

class Camion:
    def pagar(self):
        # Este método es para camiones
        print("Camión paga 6000")


# Función que usa cualquier objeto
def cobrar(vehiculo):
    # No sabemos si es carro, moto o camion
    # Solo sabemos que tiene pagar()
    vehiculo.pagar()


# Creamos objetos
c = Carro()
m = Moto()
cam = Camion()

# Usamos la misma función
cobrar(c)
cobrar(m)
cobrar(cam)