#Importación
from tabulate import tabulate
def ejercicio1():
    edades=[]#Crear lista
    nombres=[]
    apellidos=[]
    id=[]
    c=0
    while True:
        c=c+1
        print("ID:{}".format(c))
        nombre=input("Ingrese su nombre: ")
        apellido=input("Ingrese su apellido: ")
        edad=int(input("Ingrese su edad: "))
        id.append(c)
        #Ingresa los datos a las listas
        nombres.append(nombre)
        apellidos.append(apellido)
        edades.append(edad)
        res=input("Desea ingresar otra persona s/n: ")
        if res=="n" or res=="N":
            break
    print("******************************************")
    #Presentar por pantalla los datos
    for i in range(len(nombres)):
        print("{}  {}  {}  {}".format(id[i],nombres[i],apellidos[i],edades[i]))
    print("Total de personas ingresadas: {}".format(c))
#Forma 2
def ejercicio2():
    matriz=[]
    res=True#Se la creo para forzar entrar al bucle de while
    c=0
    while res == True:
        c=c+1#Contador
        print("ID: {}".format(c))
        nombre=input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        edad = int(input("Ingrese su edad: "))
        #Agregar una lista con datos  a la lista matriz
        matriz.append([c,nombre,apellido,edad])
        op=input("Desea Ingresar otra persona s/n: ")
        if op== "n" or op== "N":
            res=False #Para que salga del bucle
    matriz.append(["", "", "Total de personas:", c])
    print(tabulate(matriz, headers=["ID", "Nombre", "Apellidos", "Edad"], tablefmt="grid"))
#Ejecución
#ejercicio1()
ejercicio2()
