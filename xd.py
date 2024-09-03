class Persona:
    def __init__(self, cedula, nombre, edad):
        self.__cedula=cedula
        self.nombre=nombre
        self.edad=edad
    def setCedula(self,cedula):
        self.__cedula=cedula
    def getCedula(self):
        return self.__cedula
    def getData(self):
        return "{} {} {}".format(self.__cedula,self.nombre,self.edad)
class Empleado(Persona):
    def __init__(self,cedula, nombre, edad, sueldo):
        super().__init__(cedula,nombre,edad)
        self.__sueldo=sueldo
    def setSueldo(self,sueldo):
        self.__sueldo=sueldo
    def getSueldo(self):
        return self.__sueldo
    def getData(self):
        return "{} {} {} {}".format(self.getCedula(),self.nombre,self.edad,self.__sueldo)
    def __prueba(self, mensaje):
        print(mensaje)
class Directivo(Persona):
    def __init__(self,cedula, nombre, edad, empresa):
        super().__init__(cedula,nombre,edad)
        self.empresa = empresa
    def getData(self):
        return "{} {} {} {}".format(self.getCedula(),self.nombre,self.edad,self.empresa)
    def __prueba(self, mensaje):
        print(mensaje)
if __name__ == '__main__':
    emp=Empleado("2342432","Juan",24,23.3)
    print(emp.getData())
    emp.setSueldo(34.7)
    emp.setCedula("24082024")
    print(emp.getData())
    dicr=Directivo("2342432","Juan",24,"microsoft")
    print(dicr.getData())
    dicr.nombre="Carlos"
    dicr.setCedula("0343456")
    print(dicr.getData())