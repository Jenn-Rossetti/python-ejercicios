class Motor:
    _caballosFuerza = None
    _cantCilindros = None
    _cilindrada = None
    _tipoCombustible = None
    
    def __init__(self, cF, cC, cilindrada, tC):
        self._caballosFuerza = cF
        self._cantCilindros = cC
        self._cilindrada = cilindrada
        self._tipoCombustible = tC


    def getTipoCombustible(self):
        return self._tipoCombustible

    def setTipoCombustible(self, tipo):
        self._tipoCombustible = tipo