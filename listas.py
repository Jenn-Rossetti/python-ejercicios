primeraLista = []
sLista =[30, "jenn", 12.73, "ross", primeraLista]
#print(len(sLista))
#print(sLista[::-1])
#sLista[1] = "Carolina"
#print(sLista)
#------------------------------------------------

#crea una lista con 100 números pares  
listaDePares = [i*2 for i in range (100)]
#print(listaDePares)

#------------------------------------------------

#agregar valores a una lista vacía
usuarios = []
usuarios.append("jenn")
usuarios.append("carolina")
usuarios.append("rossetti")
#print(usuarios)
usuarios.remove("jenn")
#print(usuarios)


#------------------------------------------------

#convertir un string (o alguna estructura) en una lista
#unaLista = list(unString)
tex= "este es un texto bastante largo"
tex = list(tex)
#print(tex)

#------------------------------------------------
#separar un texto según un caracter

#texto= "este es un texto bastante largo"
#texto = texto.split(" ")
#print(texto)

#------------------------------------------------

#eliminar repetidos
unalista= [2, 3, 5, 2, 8, 9]
unSet = set(unalista) #el set no admite repetidos asi que lo convertimos a set
unalista = list(unSet) #nuevamente lo convertimos a lista
#print(unalista) #se imprime sin los repetidos

#------------------------------------------------



