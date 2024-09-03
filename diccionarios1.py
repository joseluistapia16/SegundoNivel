def ejercicio1():
    dic1 = {
        "Saludo":100,
        5:"Hola",
        (5,9,10):True,
        False: (3,5,8,"Ola"),
        10:30
    }
    dic1[False] = 1000
    del dic1[5]
    dic1["Micratf"]= (8,"Hola")
    print(dic1)
    print(len(dic1))
    print(dic1[10])
    print("*************************************************************************************")
    for clave, valor in dic1.items():
        print(f'{clave}: {valor}')
    print("*************************************************************************************")
    for valor in dic1.values():
        print(f'{valor}')
def getMenu(opc):
    for i in range(len(opc)):
        print("{}.- {}.".format((i + 1), opc[i]))
    op = -1
    while op < 1 or op > len(opc):
        op = int(input("Ingrese una opcion [1..{}]: ".format(len(opc))))
def ejercicio2():
    tupla = ("Registro", "Consulta", "Actualizar", "Eliminar", "Listar", "Salir")
    getMenu(tupla)

ejercicio2()