productosRegistrados = 0
productosConDescuento = 0
totalCompras = 0
totalPagado = 0

producto = str(input("Ingrese el nombre del producto (FIN para terminar):"))
while (producto != "FIN"):
    cantidad = int(input("Ingrese la cantidad:"))
    precio = float(input("Ingrese el precio unitario:"))

    productosRegistrados += 1

    totalProducto = cantidad * precio
    descuento = 0

    if (totalProducto >= 100000):
        descuento = totalProducto * 0.10
        productosConDescuento += 1

    elif (totalProducto >= 50000):
        descuento = totalProducto * 0.05
        productosConDescuento += 1

    valorFinal = totalProducto - descuento

    print("\nProducto: ", producto ,"\nValor original: $",totalProducto, "\nDescuento: $", descuento, "\nValor a pagar: $", valorFinal, sep="" )

    totalCompras += totalProducto
    totalPagado += valorFinal

    producto = str(input("\nIngrese el nombre del producto (FIN para terminar): "))

print("\n--- RESUMEN DE LA COMPRA ---", "\nProductos registrados: ", productosRegistrados, "\nProductos con descuento: ", productosConDescuento, "\nValor original de las compras: $", totalCompras, "\nValor final a pagar: $", totalPagado, sep="")