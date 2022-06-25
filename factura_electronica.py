def suma_todos(*args):
    print(type(args))
    return sum(args)

def consulta(**kwargs):
    print(type(kwargs))
    texto = f"Su consulta es {kwargs['fecha']} a las {kwargs['hora']}"
    return texto
consulta(fecha='hoy',hora='4PM')

valor_consulta = {"consulta":10, "arreglos_caries":20, "flúor":15}
costos = list(valor_consulta.values())

def emitir_factura(nombre, dni, tipo="DNI", *args, **kwargs):
    factura = ""
    factura += f"Gracias por su visita Nombre:{nombre} \n"
    factura += f"{tipo} {dni} \n"
    costo = suma_todos(*args) # hago unpacking de args
    factura += f"El costo es {costo} \n"
    factura += consulta(**kwargs) # hago unpacking de kwargs
    return factura

factura = emitir_factura("Obi Wan", 370310455, "DNI", *costos, fecha="hoy", hora="5PM")
print(factura)