class Persona:  ## crear la clase
    def __init__(self, nombre, edad):  ## se eejcuta cuando creas el objecto
        self.nombre = nombre  ## self respresenta el objeto que se esta creando
        self.edad = edad  ## cada sefl como edad y no,bre  guarda los datos del objeto
    def saludar(self):  ## metodo del objeto
        print("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años")


    ## metodo cumplir años
    def cumplir_anios(self):
        self.edad += 1
        print(self.nombre, "ahora tienes", self.edad, "años")


## crear un objeto
persona1 = Persona("andres", 32)
persona2 = Persona("maria", 28)


##USAR METODOS
persona1.saludar()
persona2.saludar()

persona1.cumplir_anios()
persona1.saludar()
