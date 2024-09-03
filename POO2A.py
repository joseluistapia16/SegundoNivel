class Auto:
    def __init__(self,placa,modelo,marca,color):
        self.placa=placa
        self.modelo=modelo
        self.marca=marca
        self.color=color

    def getData(self):
        return self.placa+" "+self.modelo+" "+self.marca+" "+self.color

    def prueba(self):
        self.getData()
        print("Metodo invocado")

if __name__ == '__main__':
    ob1=Auto("GMS0040","2020","Toyota","Negro")
    print(ob1.getData())
    ob1.marca="Nissan"
    ob1.modelo="2022"
    print(ob1.getData())
    ob1.prueba()

    ob2=Auto("GMS0055","2023","Mazda","Rojo")
    print(ob2.getData())
    ob2.marca="KIA"
    ob2.modelo="2009"
    print(ob2.getData())
    ob2.prueba()
    ob3=Auto("GMS0022","2024","Mercedes","Blanco")
    print(ob3.getData())
    ob3.marca="Honda"
    ob3.modelo="2018"
    print(ob3.getData())
    ob3.prueba()
    ob4=Auto("GMS0033","2009","ferrari","Azul")
    print(ob4.getData())
    ob4.marca="Hyundai"
    ob4.modelo="2020"
    print(ob4.getData())
    ob4.prueba()