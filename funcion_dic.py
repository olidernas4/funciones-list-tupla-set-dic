def cliente_info():
    cliente = {"nombre": "Andres", "vehiculos": "ABC123", "horas": 3}
    ###Agregar
    cliente["pago"] = 1500
    ## actualizar
    cliente.update({"horas": 4})
    ##obtener valor
    nombre = cliente.get("nombre")
    claves = cliente.keys()
    valores = cliente.values()
    ##eliminar
    cliente.pop("vehiculos")
    print("cliente:", cliente)
    print("nombre:", nombre)
    print("valores", valores)
cliente_info()