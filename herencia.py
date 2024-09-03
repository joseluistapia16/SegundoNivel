#herencia en programacion (que vamos a reutilizar codigo)
""" Se relaxionan por categorias """
class Vehiculo:
    def __init__(self,marca,matricula,modelo):
        self.marca=marca
        self.__matricula=matricula
        self.modelo=modelo
    def setMatricula(self,matricula):
        self.__matricula=matricula
    def getMatricula(self):
        return self.__matricula
    def getData(self):
        return "{} {} {} ".format(self.marca,self.__matricula,self.modelo)
    def __mensaje(self,msg):
        print(msg)

class Moto(Vehiculo):
    def __init__(self,marca,matricula,modelo,n_timon,n_cadena):
        super().__init__(marca,matricula,modelo)
        self.__n_timon=n_timon
        self.n_cadena=n_cadena
    def setN_timon(self,n_timon):
        self.__n_timon=n_timon
    def getN_timon(self):
        return self.__n_timon
