#Clases-- Plantillas donde se almacena cosas(Un molde en el que se pueden realizar N elementos)
#Las cclases tienen objetos adentro
#Objetos (Abdtractos o Fisicos)
#Paradigma POO
class Pelicula:
    #Metodo Constructor
    def __init__(self):
         self.nombre=""
         self.duracion=0
         self.rango_edad=0
         self.year=0
    #Metodos en clases
    def escribir(self):#Self es un indicador que nos dice que se encuentra en una clase
        print("Hola Segundo B")
        x=10#variabale local
    def suma(self,x,y):
        return (x+y)
    def prueba(self):
        self.escribir()
        print("Prueba uno")
    def prueba_1(self):
        print("Prueba dos")
        def getNombre(nombre):
            print(nombre)
    def getData(self):
        return self.nombre+" "+str(self.duracion)+" "+str(self.rango_edad)+" "+str(self.year)
if __name__ == '__main__':
    print(int("3.14"))
    pel=Pelicula()
    pel.escribir()
    pel.prueba_1()
    print("El resultado es:{}".format(pel.suma(5,10)))
    pel.nombre=input("Nombre:")
    pel.duracion=int(input("Ingrese la duracion: "))
    pel.rango_edad=int(input("Ingrese el rango: "))
    pel.year=int(input("Año: "))
    print(pel.getData())

