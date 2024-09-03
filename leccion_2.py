#Python -->Lenguaje
#C++ --> Lenguaje compilador
def inputInt(cadena):#Funcion que permite ingresar un dato
    num=-1
    while num<0:
        try:#Para evitar las excepciones
            num=int(input(cadena))
        except:#Para darnos un proceso despues de ver que hay una excepcion
            print("El valor es invalido")
    return num
#Funcion para numeros reales
def inputFloat(cadena):#Funcion que permite ingresar un dato
    num=-1
    while num<0:
        try:#Para evitar las excepciones
            num=float(input(cadena))
        except:#Para darnos un proceso despues de ver que hay una excepcion
            print("El valor es invalido")
    return num

def inputNumber(cadena):
    valor=-1
    res=True
    while res==True:
        try:
            valor = float(input(cadena))
            res=False
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
            res=True
    return valor
def getTotal(x,y):
    return x+y
def getIva(x):
    return x*0.15
def getSubtotal(x,y):
    return x*y
def ejercicio2():
    #Nombre del cliente
    cliente=input("Ingrese nombre del cliente")
    #Nombre del producto
    producto=input("Ingrese nombre del producto")
    #Valor
    valor=inputFloat("Ingrese su valor: ")
    #Cantidad
    cantidad=inputInt("Ingrese cuantos son: ")
    #Subtotal
    subtotal=getSubtotal(valor,cantidad)
    iva = getIva(subtotal)
    total = getTotal(subtotal,iva)
    msg ="Subtotal:{}\nIva:{}\nTotal a pagar:{}".format(round(subtotal,2),round(iva,2),round(total,2))
    print(msg)
ejercicio2()




def ejercicio1():
   # num=inputInt("Ingrese un numero entero: ")
    num=inputNumber("Ingrese un numero: ")

def ejercicio2():
    num=inputFloat("Ingrese un numero entero: ")

ejercicio1()
