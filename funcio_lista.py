def gestionar_vehiculos():
    vehiculos = ["ABC123", "XYZ999", "AAA111"]

    ###AGREGAR CARROS
    vehiculos.append("BBB222")
    ##INSERT
    vehiculos.insert(1, "CCC333")
    ###ELIMINAR UN VALOR
    vehiculos.remove("AAA111")
    eliminado = vehiculos.pop()
    ##ORDENAR
    vehiculos.sort()
    ##invertir
    vehiculos.reverse()
    ### contar
    cantidad = vehiculos.count("ABC123")
    ##copiar vehiculos
    copia = vehiculos.copy()

    print("lista final", vehiculos)
    print("eliminar", eliminado)
    print("cantidad ABC123", cantidad)


gestionar_vehiculos()
