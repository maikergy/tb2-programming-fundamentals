# Archivo: modules/inventario.py
from config.database import *

def modulo_inventario():
    """Muestra el submenú del módulo de inventario."""
    while True:
        print("\n--- Módulo Inventario ---")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Actualizar stock de producto")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            return
        else:
            print("Opción inválida. Intente de nuevo.")

def registrar_producto():
    """Registra un producto con validación estricta y lógica de base de datos."""
    print("\n--- Registrar Producto ---")

    while True:
        nombre = input("Ingrese nombre del producto: ").strip()
        if not nombre:
            print("El nombre no puede quedar vacío.")
            continue
        if obtener_producto_por_nombre(nombre):
            print("El producto ya existe.")
            continue
        break

    while True:
        valor_precio = input("Ingrese precio de venta: ").strip()
        try:
            precio = float(valor_precio)
            if precio <= 0:
                print("Dato inválido: el precio debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Dato inválido: ingrese un número válido para el precio.")

    while True:
        valor_stock = input("Ingrese stock inicial: ").strip()
        try:
            stock = int(valor_stock)
            if stock < 0:
                print("El stock debe ser mayor o igual a 0.")
                continue
            break
        except ValueError:
            print("Dato inválido: ingrese un número entero válido para el stock.")

    insertar_producto(nombre, precio, stock)
    print("\nProducto registrado con éxito.")
    print(f"Nombre: {nombre}, Stock inicial: {stock}")

def listar_productos():
    print("\n--- Lista de Productos ---")
    productos = obtener_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Stock: {producto[3]}")

def actualizar_producto():
    """Actualiza el stock de un producto específico."""
    
    productos = obtener_productos()

    print("\nLista de productos:")
    for prod in productos:
        print(f"ID: {prod[0]}, Nombre: {prod[1]}, Precio: {prod[2]}, Stock: {prod[3]}")

    # VALIDAR ID
    while True:
        valor_id = input("Ingrese ID del producto a actualizar: ").strip()

        try:
            producto_id = int(valor_id)
            break
        except ValueError:
            print("Dato inválido: ingrese un número entero válido para el ID.")

    producto = obtener_producto_por_id(producto_id)

    if not producto:
        print("Producto no encontrado.")
        return

    # producto = (id, nombre, precio, stock)
    _, nombre, _, _ = producto

    # VALIDAR NUEVO STOCK
    while True:
        valor_stock = input(f"Ingrese nuevo stock para '{nombre}': ").strip()
        try:
            nuevo_stock = int(valor_stock)
            if nuevo_stock < 0:
                print("El stock debe ser mayor o igual a 0.")
                continue
            break
        except ValueError:
            print("Dato inválido: ingrese un número entero válido para el stock.")

    actualizar_stock_producto(producto_id, nuevo_stock)

    print(f"Stock del producto '{nombre}' actualizado a {nuevo_stock}.")