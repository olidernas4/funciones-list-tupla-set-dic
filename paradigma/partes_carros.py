class Carro: ## creando el molde
    
    def __init__(self, marca, color): ## atributos constructor
        self.marca = marca ## cada carro tiene su propia marca
        self.color = color ## cada tiene color
        self.velocidad = 0 ## inicio
        self.encendido = False


    def encender(self):
        self.encendido = True
        print("El carro está encendido")

    def apagar(self):
        self.encendido = False
        print("El carro  está apagado")

    def acelerar(self):
        self.velocidad += 10
        print("El carro acelera. velocidad: ", self.velocidad)
    
    def frenar(self):
        self.velocidad -= 10
        if self.velocidad < 0 :
            self.velocidad = 0
        print ("el carro frena, velocidad", self.velocidad)
### el objecto 
## esto se llama intancia
carro1 = Carro("TOYOTA", "BLANCA")
carro2 = Carro("mazda", "azul")
##acciones
carro1.encender()

carro1.frenar()
carro1.frenar()
carro1.apagar()

print("------------------")

carro2.acelerar()