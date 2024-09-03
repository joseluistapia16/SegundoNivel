class Persona:
    def __init__(self, cedula, nombre, apellidos, edad):
        self.__cedula = cedula
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    def setCedula(self, cedula):
        self.__cedula = cedula
    def getCedula(self):
        return self.__cedula
    def getData(self):
        return "{} {} {} {}".format(self.__cedula, self.nombre, self.apellidos, self.edad)
    def __prueba(self, mensaje):
        print(mensaje)

class Vehiculo:
    def __init__(self, placa, marca, num_ruedas, modelo):
        self.__placa = placa
        self.marca = marca
        self.num_ruedas = num_ruedas
        self.__modelo = modelo
    def setPlaca(self, placa):
        self.__placa = placa
    def getPlaca(self):
        return self.__placa
    def setModelo(self, modelo):
        self.__modelo = modelo
    def getModelo(self):
        return self.__modelo
    def getData(self):
        return "{} {} {} {}".format(self.__placa, self.marca, self.num_ruedas, self.__modelo)
    def __prueba(self, mensaje):
        print(mensaje)