def placas_unicas():
    placas = {"ABC123", "XYZ999", "ABC123", "BBB222"}

    # AGREAGAR
    placas.add("DDD444")

    ##elminar
    placas.remove("BBB222")

    nuevas = {"EEE555", "ABC123"}
    union = placas.union(nuevas)

    diferencia = placas.difference(nuevas)

    print("placas", placas)
    print("union", union)
    print("diferencia", diferencia)


placas_unicas()
