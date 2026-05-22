# Archivo: modules/ventas.py
from datetime import datetime
from config.database import conectar

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
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT v.id, p.nombre, v.cantidad, v.total, v.fecha"
        " FROM ventas v"
        " JOIN productos p ON v.producto_id = p.id"
        " ORDER BY v.fecha DESC, v.id DESC"
    )
    ventas = cursor.fetchall()
    conexion.close()

    print("\n--- Historial de Ventas ---")
    if not ventas:
        print("No hay ventas registradas.")
        return

    for venta in ventas:
        print(f"ID: {venta[0]}, Producto: {venta[1]}, Cantidad: {venta[2]}, Total: {venta[3]}, Fecha: {venta[4]}")

def registrar_venta():
    """Registra una venta, actualiza stock y guarda el movimiento."""
    print("\n--- Registrar Venta ---")
    productos = listar_productos_disponibles()

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

    total = round(precio * cantidad, 2)
    fecha = datetime.now().strftime("%Y-%m-%d")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO ventas (producto_id, cantidad, total, fecha) VALUES (?, ?, ?, ?)",
        (producto_id, cantidad, total, fecha),
    )
    cursor.execute(
        "UPDATE productos SET stock = ? WHERE id = ?",
        (stock - cantidad, producto_id),
    )
    conexion.commit()
    conexion.close()

    print("\nVenta registrada con éxito.")
    print(f"Producto: {nombre}, Cantidad: {cantidad}, Total: {total}")

def obtener_producto_por_id(producto_id):
    """Busca un producto por su ID."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, precio, stock FROM productos WHERE id = ?", (producto_id,))
    producto = cursor.fetchone()
    conexion.close()
    return producto

def listar_productos_disponibles():
    """Lista los productos con stock mayor a cero."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, precio, stock FROM productos WHERE stock > 0")
    productos = cursor.fetchall()
    conexion.close()
    return productos