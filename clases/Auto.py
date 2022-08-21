from Vehiculo import Vehiculo
class Auto(Vehiculo):
    __marca = None
    __modelo = None

    def __init__(self, col, puer, tamanio, velMax, motor, marca, modelo):
        Vehiculo.__init__(self,col,puer,tamanio,velMax,motor)
        self.__marca = marca
        self.__modelo = modelo
    def arrancar(self):
        return("Auto arrancando...")

#esto generalmete se hace en un archivo aparte y desde ahí se importa la clase Auto

#primerAuto = Auto("Rojo", 4, "Grande", 120, 80)  #indicamos que queremos un objeto de tipo Auto
#segundoAuto = Auto("Azul",2,"Chico",240,200)  #entre parréntesis colocamos los atributos que le asignamos (color, cant puertas, tamaño,etc)
#print(primerAuto.getColor())  #uso un geter para ver el color. Para llamar a un método del auto utilizamos_
                              #el nombre de la variable donde lo creamos, punto ("."), y el método_
                              #que queremos invocar
#primerAuto.setColor("Amarillo") #hacemos lo mismo pero asignándole un valor a color usando setter
                                 #recibe un color y se lo asigna al atributo color del auto.

#print(primerAuto.getColor())

#print("El segundo auto tiene como velocidad máxima:" , segundoAuto.getVelMax())
#print("El segundo auto es de tamaño:" , segundoAuto.getTamanio())
#nuevoTam = input("Ingrese un nuevo tamanio...")
#segundoAuto.setTamanio(nuevoTam)
#print("El segundo auto es ahora de tamaño:" , segundoAuto.getTamanio())