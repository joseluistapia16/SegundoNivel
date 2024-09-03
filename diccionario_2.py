def ejercicio1():
    #Diccionarios
    #Estan colocados de forma clave
    dic_1={#Las llaves utilizan para poner los valores de claves y su contenido
        #Las claves pueden ser de distintos tipos y el valor contenido tamien
        "Saludo":50,#Lo que contiene
        10:True,#Van separados por coma pero al finalizar va sin ella
        ("uno",False,3):10.6
    }
    print(dic_1)
    #agregamos datos a una clave del diccionario
    dic_1["papa"]=10#Se agrego un caracter en la clave 10
    print(dic_1)
    #Cambiar valor
    dic_1["Saludo"]=100#Se agrego un caracter en la clave "Saludo"
    dic_1["uno"]=5000#Se agrego un caracter en la clave "uno"
    print(dic_1)
    print(dic_1[("uno",False,3)])
    print("*****************************")
    for item in dic_1.values():#Los elementos de las claves
        print(item)
    print("*****************************")
    for claves in dic_1.keys():#Las claves del
        print(claves)
    print("*****************************")
    for clave,valor in dic_1.items():#Todos los elementos incluyendo claves y su valor
        print("{} : {}".format(clave,valor))
    print("*****************************")
    del dic_1["papa"]#Para eliminar elemento
    print(dic_1)
    dic_1.pop(10)#Para eliminar elemento
    print(dic_1)
    dic_1.clear()#Eliminar todos los elementos
    print("Tamaño:{}".format(len(dic_1)))
    #Son partes de una fila
    #Los diccionarios son aquellos que pueden guardar varios datos en una solo clave.
def getMenu(opc):
    for i in range(len(opc)):
        print("{}.- {}.".format((i+1),opc[i]))
    op=-1
    while op<1 or op>len(opc):
        op=int(input("Ingrese una opcion[1...{}]:".format(len(opc))))
    return op
def ejercicio2():
    tupla=("Registro","Consulta","Actualizar","Eliminar","Listar","Salir")
    op=getMenu(tupla)
#Llamar a las funciones para ejevutarlas
ejercicio2()