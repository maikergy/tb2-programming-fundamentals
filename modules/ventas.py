# Archivo: modules/ventas.py
from datetime import datetime
from config.database import *

def modulo_ventas():
    """Muestra el submenú del módulo de ventas."""
    while True:
        print("\n--- Módulo Ventas ---")
        print("1. Registrar Venta")
        print("2. Historial de Ventas")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
            return
        else:
            print("Opción inválida. Intente de nuevo.")

def listar_ventas():
    """Muestra el historial de ventas guardado en la base de datos."""
    ventas = obtener_ventas()

    print("\n--- Historial de Ventas ---")
    if not ventas:
        print("No hay ventas registradas.")
        return

    for venta in ventas:
        print(f"Producto: {venta[0]}, Cantidad: {venta[1]}, Total: {venta[2]}, Fecha: {venta[3]}")

def registrar_venta():
    """Registra una venta, actualiza stock y guarda el movimiento."""
    print("\n--- Registrar Venta ---")
    productos = obtener_productos_disponibles()

    if not productos:
        print("No hay productos con stock disponible.")
        return

    print("\nProductos disponibles:")
    for prod in productos:
        print(f"ID: {prod[0]}, Nombre: {prod[1]}, Precio: {prod[2]}, Stock: {prod[3]}")

    while True:
        valor_id = input("Ingrese ID del producto a vender: ").strip()
        try:
            producto_id = int(valor_id)
            break
        except ValueError:
            print("Dato inválido: ingrese un número entero válido para el ID.")

    producto = obtener_producto_por_id(producto_id)
    if not producto:
        print("Producto no encontrado.")
        return

    _, nombre, precio, stock = producto

    while True:
        valor_cantidad = input("Ingrese cantidad a vender: ").strip()
        try:
            cantidad = int(valor_cantidad)
            if cantidad <= 0:
                print("Dato inválido: la cantidad debe ser mayor a 0.")
                continue
            if cantidad > stock:
                print(f"Stock insuficiente. Stock disponible: {stock}.")
                continue
            break
        except ValueError:
            print("Dato inválido: ingrese un número entero válido para la cantidad.")

    total = precio * cantidad
    fecha = datetime.now().strftime("%Y-%m-%d")

    insertar_venta_y_actualizar_stock(producto_id, cantidad, total, fecha)

    print("\nVenta registrada con éxito.")
    print(f"Producto: {nombre}, Cantidad: {cantidad}, Total: {total:.2f}")