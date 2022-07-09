nombre = input("Bienvenido, ingrese su nombre...")
print("Hola", nombre , ". Por favor, elija una de las siguientes opciones...")

print("1- detectar mayor de 3 números\n2- identificar un horario\n3- Decidir si suma de cifras es un número de cifras par o impar\n4- Descomponer un número de 5 dígitos y mostrarlos invertidos")

opc = int(input("ingresá tu selección..."))
if(opc == 1):
    print("elegida opción 1...")
    print("ingrese 3 números enteros. Vamos a detectar cuál es el mayor...")
    numA = int(input("primer número..."))
    numB = int(input("segundo número..."))
    numC = int(input("tercer número..."))
    if (numA >= numB and numA >= numC):
        print("El mayor es el ", numA)
    elif (numB >= numA and numB >= numC):
        print("El mayor es el ", numB)
    else:
        print("El mayor es el ", numC)
    #algoritmo simplificado
    #(numA > numB and numB > numC) -> el mayor es A
    #porque si B es mayor a C, A también es mayor a C porque es mayor a B.
elif opc == 2:
    print("elegida opción 2...")
    hora = int(input("ingrese una hora para saber si es de mañana, tarde o noche"))
    if (hora > 12):
        print("Es de mañana")
    elif (12 >= hora < 18 ):
        print(" Es de tarde")
    elif (hora > 18) :
        print("Es de noche")

elif opc == 3:
    print("elegida opción 3...")
    numero3cifras = int(input("ingrese un número de 3 cifras..."))
    numero3cifras = str(numero3cifras)
    numero3cifras = list(numero3cifras)
    numero3cifras[0] = int(numero3cifras[0])
    numero3cifras[1] = int(numero3cifras[1])
    numero3cifras[2] = int(numero3cifras[2])
    suma = numero3cifras[0] + numero3cifras[1] + numero3cifras[2]
    print("la suma de los tres dígitos es..." , suma)
    if (suma %2 == 0):
      print("La suma es par")
    else:
      print("la suma es impar")
      
else:
    print("elegida opción 4...")
    numero = int(input("ingrese un número de 3 cifras..."))
    numero = str(numero)
    numero = list(numero)
    numero[0] = int(numero[0])
    numero[1] = int(numero[1])
    numero[2] = int(numero[2])
    numero[3] = int(numero[3])
    numero[4] = int(numero[4])
#guardar los pares
    lNueva = []
    if(numero[0] %2 == 0):
        lNueva.append(numero[0])
    if(numero[1] %2 == 0):
        lNueva.append(numero[1])
    if(numero[2] %2 == 0):
        lNueva.append(numero[2])
    if(numero[3] %2 == 0):
        lNueva.append(numero[3])
    if(numero[4] %2 == 0):
        lNueva.append(numero[4])
#imprimirla al revés
    print(lNueva[::-1])
