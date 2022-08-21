from msilib.schema import ListView


def aMinúscula(texto):
    return texto.lower()
#----------

def saludar(nom, apellido):
    return ("Bienvenido" + " " + nom + " " + apellido)
print(saludar("Jenn", "Rossetti"))
#-----------

def tieneVocales(texto):
    vocales = False
    if ("a" in texto) or ("e" in texto) or ("i" in texto) or ("o" in texto) or ("u" in texto):
      vocales = True
    return (texto, vocales)
print(tieneVocales("este texto sí tiene vocales"))
#------------

def cuentaVocales(texto):
    lVocales = ["a","e","i","o","u"]
    cVocales = [0,0,0,0,0]
    for letra in texto:
        if letra == "a":
            cVocales[0] = cVocales[0]+1
        elif letra == "e":
            cVocales[1] = cVocales[1]+1
        elif letra == "i":
            cVocales[2] = cVocales[2]+1
        elif letra == "o":
            cVocales[3] = cVocales[3]+1
        elif letra == "u":
            cVocales[4] = cVocales[4]+1
    return (lVocales, cVocales)
print(cuentaVocales("Este teto tiene vocales"))

#------------
        
def saludoDos(nombre = "persona", apellido = "desconocida"):
    return ("Bienvenido" + " " + nombre + " " + apellido)

    
print(saludoDos("Jenn", "Rossetti"))

#------------
#Función LAMBDA - versión de saludoDos en lambda
saludando = lambda nom, ap:("Hola " + " " + nom + " " + ap)
print(saludando("jenn", "rossetti"))
#------------
#pares menores a n
def paresMenores(n):
    resultado = []
    i = 0
    while(i<=n):
        if(i%2 == 0):
            resultado.append(i)
        i = i+1
    return resultado


def esPrimo(n):
    primo = True
    i = 2
    while(i<n//2):
        #print("Dividiendo ", n , " por " , i)
        if(n%2 == 0):
            primo = False
        i = i+1
    return primo