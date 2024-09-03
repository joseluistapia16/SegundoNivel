from tabulate import tabulate # importar el paquete externo tabulate
def getSubtotal(precio,cantidad):
    return (precio*cantidad)
def getIva(subtotal):
    return (subtotal*0.15)
def getTotal(subtotal,Iva):
    return (subtotal+Iva)

def funcion():
    c=0
    ac=0
    while c<10:
        c=c+1
        if c%2==0:
           ac=ac+c
           print(c)
    print("el total acumulado es:{}".format(ac))

def funcion2():
    ac=0
    for c in range(1,11):
        if c%2==0:
           ac=ac+c
           print(c)
    print("el total acumulado es:{}".format(ac))

def factura():
    totalA=0
    nombre=input("Cliente: ")
    numero=int(input("Cuantos productos va a comprar: "))
    tablas_filas=[]
    for c in range(numero):
        producto=input("Producto: ")
        precio=float(input("Precio: "))
        cantidad=int(input("Cantidad: "))
        sub=getSubtotal(precio,cantidad)
        iva=getIva(sub)
        total=getTotal(sub,iva)
        msg="El subtotal es: {}\nEl  Iva es: {}\nTotal: {}\n ".format(round(sub),round(iva),round(total,2))
        print(msg)
        totalA=totalA+total
        tablas_filas.append([producto,precio,cantidad,round(sub,2),round(iva,2),round(total,2)])
    tablas_filas.append(["","","","","Total a pagar: ",round(totalA,2)])
    print(tabulate(tablas_filas, headers=["Producto", "Precio", "Cantidad", "Subtotal", "Iva", "Total"],tablefmt="grid"))
    #print("El total a pagar es: {}".format(round(totalA,2)))

def ejercicio11():
    while True:
        respuesta = input("Desea agregar otro elemento [s - n]? ")
        if respuesta == "n" or respuesta == "N":
            break
#funcion()
#funcion2()
#factura()
ejercicio11()
