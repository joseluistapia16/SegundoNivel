class Operacion:
    def __init__(self,valor_1,valor_2):
        self.valor_1=valor_1
        self.valor_2=valor_2
    def getData(self):
        return "{}  {}".format(self.valor_1,self.valor_2)

    def getSuma(self):
        return (self.valor_1+self.valor_2)
    def getResta(self):
        return (self.valor_1 - self.valor_2)
    def getMultiplicacion(self):
        return (self.valor_1 * self.valor_2)
    def getDivision(self):
        return (self.valor_1/self.valor_2)

class Vehiculo:
    def __init__(self,placa,marca,color,n_ruedas):
        self.placa=placa
        self.marca=marca
        self.color=color
        self.n_ruedas=n_ruedas

    def getData(self):
        return " {} {} {} {} ".format(self.placa,self.marca,self.color,self.n_ruedas)

def ejemplo_1():
    ob1 = Operacion(10, 7)
    print(ob1.getData())
    print("El resultado de la suma es: {}".format(ob1.getSuma()))
    print("El resultado de la resta es: {}".format(ob1.getResta()))
    print("El resultado de la multipliación es: {}".format(ob1.getMultiplicacion()))
    print("El resultado de la división es: {}".format(ob1.getDivision()))

def ejemplo_2():
    ob=Vehiculo("GSG200","Toyota","Blanco",4)
    print(ob.getData())
    ob.marca="Mazda"
    ob.n_ruedas=6
    print(ob.getData())
    print("****************************")
    u=Vehiculo("100JRR","Audi","Azul",4)
    print(u.getData())
    print("--------------------")
    u.color="Blanco"
    print(u.getData())
    print("***************************")
    d=Vehiculo("0820RRJL","Ford","Gris",6)
    print(d.getData())
    print("--------------------")
    d.n_ruedas=4
    d.color="Dorado"
    print(d.getData())
    print("****************************")
    t=Vehiculo("RJRL","Suzuki","Negro",4)
    print(t.getData())
    print("------------------------")
    t.marca="Ferrari"
    t.color="Rojo"
    print(t.getData())
    print("I---------------------------------------------I")



if __name__ == '__main__':
    ejemplo_2()
