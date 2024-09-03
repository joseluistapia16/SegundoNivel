from tabulate import tabulate #Libreria Tabulate
def ejercicio1():
    while True:
        op=input("Dese otro articulo[s/n]:")
        if op=="n" or op=="N":#Colocamos parametros
            break

#Factura
def factura():
    sub_ac_1=0#Subtotales
    iva_ac_2 = 0 #Iva
    pro_ac_3 = 0#Producto
    cliente=input("Ingrese el nombre del cliente:")
    tabla_filas=[]  #Creacion de lista
    while True:
        producto=input("Ingrese el nombre del producto: ")
        precio=float(input("El precio: "))
        cantidad=int(input("Ingrese la cantidad: "))
        subtotal=(precio*cantidad)
        iva=(subtotal*0.15)
        total=(subtotal+iva)
        msj="Subtotal:{}\nIva:{}\nTotal:{}".format(round(subtotal,2),round(iva,2),round(total,2))
        print(msj)
        tabla_filas.append([producto,precio,cantidad,round(subtotal,2),round(iva,2),round(total,2)])#Items comienzan desde 0 en lista
        sub_ac_1=sub_ac_1+subtotal#Acumulador de Subtotal
        iva_ac_2=iva_ac_2+iva#Acumulador de Iva
        pro_ac_3=pro_ac_3+total#Acumulador de Total
        op=input("Dese otro articulo[s/n]:")
        if op=="n" or op=="N":
            break
    tabla_filas.append(["", "", "", "", "Subtotal:", round(sub_ac_1, 2)])
    tabla_filas.append(["", "", "", "", "Iva:", round(iva_ac_2, 2)])
    tabla_filas.append(["", "", "", "", "Total a pagar es:", round(pro_ac_3, 2)])
    print(tabulate(tabla_filas,headers=["Producto","Precio","Cantidad","Subtotal","Iva","Total"],tablefmt="grid"))#Forma de la representacion de las lines}as en el marco
   # print("El total a pagar es:{}".format(round(pro_ac_3,2)))
factura()