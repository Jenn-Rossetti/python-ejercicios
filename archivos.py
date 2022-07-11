arc = open("arcTexto.txt", "r")
arc.close()
#código base para leer el archivo
file = open("arcTexto.txt", "r")
for linea in file:
   print(linea)
file.close()