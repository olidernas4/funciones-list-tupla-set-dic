####contar hacia atras

def contar(numero):
    ###caso base
    if numero == 10:
        print("final")
        return   
    #mostrar
    print(numero)
    #llamada recursividad
    contar(numero +1)

contar(5)