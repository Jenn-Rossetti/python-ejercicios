class Vehiculo:
    #atributos
    _color = None #protected
    _puertas = None #tienen asignados el valor none porque se inicializan vacíos
    _tamanio = None
    _velMaxima_velMaxima = None
    _motor = None

    def __init__(self, col, puer, tamanio, velMax, motor): #método constructor
        self._color = col #cada que creamos un objeto del tipo vehículo (x ej.), vamos a poder
        self._puertas = puer #indicarle entre paréntesis sus atributos color, puertas, tamaño, etc.
        self._tamanio = tamanio
        self._velMaxima = velMax
        self._motor = motor


    def getColor(self): #getters. Método que tiene como única función retornar el valor
        return self._color #(o atributo color en este caso) del vehículo (la clase)

    def setColor(self,color): #Setters. toma como parámetro un color y se le asigna al atributo_
        self._color = color #color del propio auto. Es para darle color al auto.
        
    def getPuertas(self):
        return self._puertas

    def setPuertas(self,puertas):
        self._puertas = puertas

    def getTamanio(self):
        return self._tamanio

    def setTamanio(self, tamanio):
        self._tamanio = tamanio

    def getVelMax(self):
        return self._velMaxima

    def setVelMax(self,velMax):
        self._velMaxima = velMax

    def getMotor(self):
        return self._motor

    def arrancar(self):
        return "Vehículo arrancando..."
        
    def __str__(self):
        return "Color: " + self._color + " | Tamaño: " + self._tamanio + " | V max:  " + str(self._velMaxima)
    

#primerAuto = Auto("Rojo", 4, "Grande", 120, 80)
#segundoAuto = Auto("Azul",2,"Chico",240,200)
#print(primerAuto.getColor())

#primerAuto.setColor("Amarillo")

#print(primerAuto.getColor())

#print("El segundo auto tiene como velocidad máxima:" , segundoAuto.getVelMax())
#print("El segundo auto es de tamaño:" , segundoAuto.getTamanio())
#nuevoTam = input("Ingrese un nuevo tamanio...")
#segundoAuto.setTamanio(nuevoTam)
#print("El segundo auto es ahora de tamaño:" , segundoAuto.getTamanio())
