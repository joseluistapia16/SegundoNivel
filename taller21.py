from tabulate import tabulate
def getAverage(n1,n2,n3):
    return(n1+n2+n3)/3
def getMessage(prom):
    if prom>=0 and prom<7:
        return("Reprobado")
    if prom>=7 and prom<=10:
        return("Aprobado")
    if prom<0 or prom>10:
        return("Valor invalido")

def ejercicio1():
    ac=0
    c=0
    tabla_filas=[]
    while True:
        print("Estudiante #{}".format(c+1))
        nombre=input("El nombre del estudiante: ")
        asignatura=input("Nombre de la asignatura: ")
        n1=float(input("Nota 1: "))
        n2=float(input("Nota 2: "))
        n3=float(input("Nota 3: "))
        prom=getAverage(n1,n2,n3)
        msg=getMessage(prom)
        if msg=="Valor invalido":
            prom=0
        print("El promedio es: {}\n{}".format(round(prom,2),msg))
        c=c+1
        ac=ac+prom
        tabla_filas.append([nombre,asignatura,n1,n2,n3,round(prom,2),msg])
        op=input("Desea agregar otro estudiante[S/N]:")
        if op=="n" or op=="N":
           break
    ac=ac/c
    tabla_filas.append(["","","","","","El promedio general es:",round(ac,2)])
    print(tabulate(tabla_filas,headers=["Estudiante","Asignatura","Nota 1","Nota 2","Nota 3","Promedio","Estado"],tablefmt="grid"))
    #print("El promedio general es: {}".format(round(ac,2)))
ejercicio1()
