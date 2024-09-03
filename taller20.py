from tabulate import tabulate #importar el paquete externo tabulate
def getPromedio(n1,n2,n3):
    return (n1+n2+n3)/3
def getMensaje(promedio):
    if promedio >=0 and promedio <7:
        return ("Reprobado")
    if promedio >=7 and promedio <=10:
        return ("Aprobado")
    if promedio <0 or promedio >10:
        return ("Invalido")
def ejercicio1():
    ac=0
    c=0
    tabla_filas=[]
    while True:
        print("Estudiante #"+str(c+1))
        nombre=input("Nombre:")
        asignatura=input("Asignatura:")
        nota1 = float(input("Nota 1:"))
        nota2 = float(input("Nota 2:"))
        nota3 = float(input("Nota 3:"))
        prom= getPromedio(nota1,nota2,nota3)
        msg= getMensaje(prom)
        print("Promedio:{}\n{}".format(round(prom,2),msg))
        if msg=="Invalido":
            prom=0
        tabla_filas.append([nombre, asignatura, nota1, nota2, nota3, round(prom, 2), msg])
        c=c+1
        ac=ac+prom
        op=input("Desea agregar otro estudiante[S/N]:")
        if op== "n" or op== "N":
            break
    ac = ac / c
    tabla_filas.append(["","","","","","Promedio general:",round(ac,2)])
    print("Numeros de estudiantes ingresados:{}".format(c))
#    print("Promedio general:{}".format(round(ac,2)))
    print(tabulate(tabla_filas,headers=["Estudiante","Asignatura","Nota 1","Nota 2","Nota 3","Promedio","Estado"],tablefmt="grid"))
ejercicio1()