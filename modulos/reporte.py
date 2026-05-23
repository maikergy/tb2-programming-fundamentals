# INTERFAZ DE MODULO REPORTES:
def modulo_reportes():

    while True:

        print("\n===== MODULO REPORTES =====\n")
        print("1. Productos con stock critico")
        print("2. Producto mas vendido")
        print("3. Productos sin ventas")
        print("4. Ganancias totales")
        print("5. Volver")

        opcion = input("\nElija una opcion: ")

        # VALIDACION DE DATO INGRESADO:
        if not opcion.isdigit():
            print("Error: ingrese un numero valido.")
            continue

        opcion = int(opcion)

        if opcion == 1:
            reporte_stock_critico(productos)

        elif opcion == 2:
            reporte_producto_mas_vendido(ventas)

        elif opcion == 3:
            reporte_productos_sin_ventas(productos, ventas)

        elif opcion == 4:
            reporte_ganancias_totales(ventas)

        elif opcion == 5:
            return

        else:
            print("Opcion invalida.")


# REPORTE DE STOCK CRITICO:
def reporte_stock_critico(productos):

    minimo = 10
    encontrados = False

    print("\n===== PRODUCTOS CON STOCK CRITICO =====\n")

    for producto in productos:

        # producto[3] = stock

        if producto[3] <= minimo:

            print(f"Producto: {producto[1]}")
            print(f"Stock: {producto[3]}")
            print("\n")

            encontrados = True

    if not encontrados:
        print("No hay productos con stock critico.")




# PRODUCTO MAS VENDIDO:
def reporte_producto_mas_vendido(ventas):

    print("\n===== PRODUCTO MAS VENDIDO =====\n")

    mayor_cantidad = 0
    producto_mas_vendido = ""

    for venta in ventas:

        #  venta[2] = cantidad vendida

        if venta[2] > mayor_cantidad:

            mayor_cantidad = venta[2]
            producto_mas_vendido = venta[1]

    if mayor_cantidad == 0:

        print("No hay ventas registradas.")

    else:

        print(f"Producto mas vendido: {producto_mas_vendido}")
        print(f"Cantidad vendida: {mayor_cantidad}")




# PRODUCTOS SIN VENTAS:
def reporte_productos_sin_ventas(productos, ventas):

    print("\n===== PRODUCTOS SIN VENTAS =====\n")

    encontrados = False

    for producto in productos:

        vendido = False

        for venta in ventas:

            # producto[1] = nombre
            # venta[1] = nombre_producto

            if producto[1] == venta[1]:

                vendido = True

        if not vendido:

            print(f"Producto: {producto[1]}")
            print(f"Stock: {producto[3]}")
            print("\n")

            encontrados = True

    if not encontrados:
        print("Todos los productos tienen ventas.")




# GANANCIAS TOTALES:
def reporte_ganancias_totales(ventas):

    print("\n===== GANANCIAS TOTALES =====\n")

    ganancias_totales = 0

    for venta in ventas:

        # venta[3] = total
        ganancias_totales += venta[3]

    print(f"Ganancias totales: S/. {ganancias_totales}")