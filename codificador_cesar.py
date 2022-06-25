def codificador_cesar(mensaje_path, clave):
    # Un ayudin
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    # Ahora hagan su magia (ojo con las mayúsculas)
    # Llamamos a upper para obtener sólo minúsculas
    with open(mensaje_path, 'r') as f:
        contenido = f.read().lower()
        # Variable para guardar mensaje cifrado
        cifrado = ""
        for l in contenido:
            # Si la letra está en el abecedario se reemplaza
            if l in abecedario:
                pos_letra = abecedario.index(l)
                # Sumamos para movernos a la derecha del abc
                nueva_pos = (pos_letra + clave) % len(abecedario)
                cifrado+= abecedario[nueva_pos]
            else:
                # Si no está en el abecedario sólo añadelo
                cifrado+= l
    #print(cifrado)
    return cifrado