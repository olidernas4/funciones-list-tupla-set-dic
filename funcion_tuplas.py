def datos_parqueadero():
    info = ("buga centro", "cali", 50)
    nombre = info [0]
    ciudad = info [1]

    # contar
    veces = info.count("cali")
    ##buscar indice
    posicion = info.index(50)

    print("nombre:", nombre)
    print("veces cali", veces)
    print("posicion o capacidad", posicion)
    print("ciudad", ciudad)


datos_parqueadero()
