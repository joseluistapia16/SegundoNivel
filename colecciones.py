#Estructura de datos
#Una dupla, es inmutable(no le puede aumentar ni quitar su valor ni cambiar)
from tabulate import tabulate


def Tupla():
    datos = ("Auto", 30, True)
    print(datos[2])
    print(datos)
    datos = ("Hola", False, 1.10, "Dos A", 20)
    for i in range(len(datos)):
        print(datos[i])
#Las listas, son mutables
def Listas():
    lista=["Bernardino",100,True,2.55]
    #print (lista)
    #print (lista[1])
    for i in range (len(lista)):
        print (lista[i])
    print("Longitud: {}".format(len(lista)))
    lista.append(300)
    lista.append("Informatica")
    print("Longitud: {}".format(len(lista)))
    print(lista)
    lista.pop(2)
    print("Longitud: {}".format(len(lista)))
    lista[1]=1000
    print(lista)
    lista.clear()
    print("Longitud: {}".format(len(lista)))
def Lista1():
    lista=[]
    print("Longitud: {}".format(len(lista)))
    nombre=input("Nombre: ")
    edad=int(input("Edad: "))
    lista.append(nombre)
    lista.append(edad)
    print (lista)
def Lista2():
    lista=[]
    for i in range(5):#Bucle para ingresar datos en la lista
        nombre=input("Nombre: ")
        lista.append(nombre)
    print("Longitud: {}".format(len(lista)))
    for i in range (len(lista)):#Bucle para mostar los datos de la lista
        print (lista[i])

def lista3():
    lista = []
    for i in range(5):  # Bucle para ingresar datos en la lista
        nombre = int(input("Numero: "))
        lista.append(nombre)
    print("Longitud: {}".format(len(lista)))
    for i in range(len(lista)):  # Bucle para mostar los datos de la lista
        print(lista[i])
def lista4():
    lista = []
    for i in range(6):  # Bucle para ingresar datos en la lista
        nombre = input("Nombre: ")
        edad= int(input("Edad: "))
        lista.append(nombre)
        lista.append(edad)
    print("Longitud: {}".format(len(lista)))
    for i in range(len(lista)):  # Bucle para mostar los datos de la lista
        print(lista[i])

def lista5():
    matriz = [[1, 2, 3, 4],
              [5, 6, 7, 8]]

    # Imprimir la matriz
    for fila in matriz:
        print(fila)

def getPosition(id, lista):
    pos=0
    for i in range(len(lista)):
        if id == lista[i][0]:
            pos=i
            break
    return pos
def lista6():
    matriz = []
    i=1
    while True:
        print("Estudiante #{}".format(i))
        nombre = input("Nombre:")
        apellido = input("Apellido:")
        edad = input("Edad:")
        matriz.append([i,nombre,apellido,edad])
        op= input("Desea agregar otro estudiante[S/N]:")
        if op=="N" or op=="n":
            break
        i=i+1
    matriz.append(["","","Total de estudiantes:",i])
    print(tabulate(matriz, headers=["ID","Nombre", "Apellidos", "Edad"],tablefmt="grid"))
    id = int(input("Id:"))
    pos = getPosition(id,matriz)
    if pos!=0:
        print(matriz[pos][0],matriz[pos][1],matriz[pos][2],matriz[pos][3])
    else:
        print("ID no existe!")
def lista7():
    matriz = []
    c = 0
    while True:
        c = c + 1
        print("ID: {}".format(c))
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        matriz.append([c, nombre, apellido, edad])
        res = input("¿Desea agregar otra persona? S/N: ")
        if res == "n" or res == "N":
            break
    matriz.append(["", "", "Total de personas: ", c])
    print(tabulate(matriz, headers=["ID:", "Nombres:", "Apellidos:", "Edades:"], tablefmt="grid"))

lista7()
