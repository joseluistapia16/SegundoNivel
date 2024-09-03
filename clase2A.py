class Persona:

    def __init__(self):
        self.cedula = ""
        self.nombre = ""
        self.apellido = ""
        self.edad = 0
    def escribir(self):
        print("Hola mundo.")
    def suma(self, x, b):
        return (x + b)
    def prueba(self):
        self.escribir()
    def getData(self):
        return self.cedula + " " + self.nombre + " " + self.apellido + " " + str(self.edad)

if __name__ == '__main__':

    per = Persona()
    per.cedula = "0984575487"
    per.nombre = "Hector"
    per.apellido = "Drouet"
    per.edad = 16
    print(per.getData())
    print("El resultado es: {}".format(per.suma(10, 30)))