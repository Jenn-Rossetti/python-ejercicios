#from funciones import cuentaVocales #desde la carpeta funciones importamos la función cuentaVocales
#from funciones import * # importa todo lo que hay en funciones
#print(cuentaVocales("Hola esto es un texto"))

#----------------
#generar números aleatorios

import random
aleatorio = random.randint(1, 10) #randint produce un número entero aleatorio
print(aleatorio)

#------------------
#importa el módulo funciones

import funciones

#Si se importo bien entonces cuenta las vocales del texto que le pasé
print(funciones.cuentaVocales("hola jennifer"))
