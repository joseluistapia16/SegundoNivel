
from tabulate import tabulate

# Definición de los elementos de la factura
productos = [
    {"producto": "Producto A", "precio": 150.50, "cantidad": 2},
    {"producto": "Producto B", "precio": 100.25, "cantidad": 3},
    {"producto": "Producto C", "precio": 75.80, "cantidad": 1},
]

# Calcular el total a pagar
total_a_pagar = 0
for prod in productos:
    prod["total"] = prod["precio"] * prod["cantidad"]
    total_a_pagar += prod["total"]

# Crear una lista de filas para la tabla
tabla_filas = []
for prod in productos:
    tabla_filas.append([prod["producto"], f"${prod['precio']:.2f}", prod["cantidad"], f"${prod['total']:.2f}"])

# Agregar una fila para el total
tabla_filas.append(["", "", "Total a pagar:", f"${total_a_pagar:.2f}"])

# Imprimir la tabla usando tabulate
print(tabulate(tabla_filas, headers=["Producto", "Precio", "Cantidad", "Total"], tablefmt="grid"))