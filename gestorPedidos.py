####### Declaramos nuestro diccionario de productos ######
codigos = [143,568,991,321]

nombresPrecios = [("Disco rígido SSD",5000), ("Mouse inalámbrico",800), ("Teclado bluetooth",1000), ("Memoria 8GB",5000)]

datos = dict(zip(codigos, nombresPrecios))

pedido = [] 

print(" ---- Programa gestor de pedidos ---- ")
nombre = input("Por favor, ingrese su nombre...")
print("Estimado " , nombre , " a continuación confeccionaremos su lista de pedidos.")


cods = list(datos.keys()) 

codigo = -2

while(codigo!=-1) :
    print("Lista de códigos disponibles para agregar:")

    for i in range(len(cods)) :
        print(cods[i])
    codigo = int(input("¿Qué código desea agregar al pedido? (Ingrese -1 para finalizar)"))

    if(codigo!=-1):
        datosAInsertar = datos.get(codigo)
        pedido.append(datosAInsertar)
        print("Producto cargado con éxito")
    
    print("----------------------------------------")

print("Tu pedido consiste de: ")
for elemento in pedido:
    print("Nombre del producto: ", elemento[0], " | Precio: ", elemento[1])

#Recuperamos las claves del diccionario, mostrando los codigos. De éstos deberá elegir el usuario.
cods = list(datos.keys()) 
