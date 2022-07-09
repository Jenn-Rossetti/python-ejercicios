condicion =(2 != 3)
i = 0
while(i < 20):
    #print("contando..." , i)
    i = i + 1

#---------------------------------
#contraseña 

palabraSecreta = "wendy"
#acertijo = input("ingresá una palabra y adiviná si es la clave...")
#while(acertijo != palabraSecreta):
   # print("Error, esa no es la clave")
   # acertijo = input("ingresá una palabra y adiviná si es la clave...")

#----------------------------------
#recorrer una lista

lista = [98, 7, 12, 5, "r", 9]
i=0
while(i < len(lista)):
  #  print(lista[i])
    i = i + 1

#----------------------------------
#palabras con a

lPalabras = ["murciélago", "oficial", "hoy", "té"]
lConA = []
i = 0
#while(i < len(lPalabras)):
   # if("a" in lPalabras[i]):
    #    lConA.append(lPalabras[i])
    #    i = i + 1
    #    print(lConA)

#----------------------------------
#buscador de palabras

palBuscada = input("Ingrese una palabra para ver si está presente en la lista o escriba FIN para cerrar el programa: ")

while(palBuscada != "FIN"):
    if palBuscada not in lPalabras:
        print("La palabra que querés buscar no está en la lista...")
    else:
        for i in range(len(lPalabras)):
            if(lPalabras[i] == palBuscada):
                lConA.append(lPalabras[i])
        print("Palabra encontrada: ", lConA)
    palBuscada = input("Ingrese una palabra para ver si está presente en la lista o escriba FIN para cerrar el programa: ")

#-----------------------------------
