from tabulate import tabulate # importar el paquete externo tabulate
def bucle():
    c = 0
    ac = 0
    while c < 10:
        c = c + 1
        if c % 2 != 0:
            ac = ac + c
            print(c)
    print("El total acumulado es: {}". format(ac))

def bucle2():
    ac = 0
    for c in range(1,11):
        if c % 2 != 0:
            ac = ac + c
            print(c)
    print("El total acumulado es: {}". format(ac))
def factura():
    ac = 0
    asb =0
    aiv =0
    cliente = input("Cliente: ")
    n = int(input("Cuantos productos va a comprar?: "))
    tabla_filas = []  # Crear una lista vacia
    for c in range(n):
        print("Item: {}".format(c + 1))
        producto = input("Producto: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        subtotal = (precio * cantidad)
        iva = (subtotal * 0.15)
        total = (iva + subtotal)
        msg = "Subtotal: {}\nIva: {}\nTotal: {}\n". format(round(subtotal,2),round(iva,2),round(total,2))
        print(msg)
        #Agregar filas en la tabla , por medio de la lista que contiene los valores
        tabla_filas.append([producto,precio, cantidad, round(subtotal,2),round(iva,2),round(total,2)])
        asb = asb + subtotal
        aiv= aiv + iva
        ac= ac + total
    tabla_filas.append(["", "", "", "", "Subtotal:", round(asb,2)])
    tabla_filas.append(["", "","" ,"","Iva:",round(aiv,2)])
    tabla_filas.append(["", "","" ,"","Total a pagar:",round(ac,2)])
    print(tabulate(tabla_filas, headers=["Producto", "Precio", "Cantidad","Subtotal","Iva", "Total"], tablefmt="grid"))
factura()
