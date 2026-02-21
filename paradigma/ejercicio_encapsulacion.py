##EJERCICIO 1 — ENCAPSULACIÓN
##Proteger datos dentro de una clase

# ENCAPSULACIÓN

class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.__saldo = saldo   # Privado con __

    def ver_saldo(self):
        # Método para ver saldo
        print("Saldo:", self.__saldo)

    def pagar(self, valor):
        # Modificar saldo de forma segura
        if valor <= self.__saldo:
            self.__saldo -= valor
            print("Pago realizado")
        else:
            print("Saldo insuficiente")

c = Cliente("Andrés", 50000)

c.ver_saldo()
c.pagar(20000)
c.ver_saldo()

# c.__saldo x ERROR porque es privado