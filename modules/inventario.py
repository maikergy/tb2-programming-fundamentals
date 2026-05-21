# Archivo: modules/inventario.py
from config.database import conectar

def modulo_inventario():
    """Muestra el submenú del módulo de inventario."""
    while True:
        print("\n--- Módulo Inventario ---")
        print("1. Registrar Producto")
        print("2. Listar Productos")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            return
        else:
            print("Opción inválida. Intente de nuevo.")

def registrar_producto():
    """Registra un producto con validación estricta y lógica de base de datos."""
    print("\n--- Registrar Producto ---")

    while True:
        nombre = input("Ingrese nombre del producto: ").strip()
        if nombre:
            break
        print("Dato inválido: el nombre no puede quedar vacío.")

    while True:
        valor_precio = input("Ingrese precio de venta: ").strip()
        try:
            precio = float(valor_precio)
            if precio > 0:
                break
            print("Dato inválido: el precio debe ser mayor a 0.")
        except ValueError:
            print("Dato inválido: ingrese un número válido para el precio.")

    while True:
        valor_stock = input("Ingrese stock inicial: ").strip()
        try:
            stock = int(valor_stock)
            if stock >= 0:
                break
            print("Dato inválido: el stock debe ser mayor o igual a 0.")
        except ValueError:
            print("Dato inválido: ingrese un número entero válido para el stock.")

    insertar_producto(nombre, precio, stock)
    print("\nProducto registrado con éxito.")
    print(f"Nombre: {nombre}, Stock inicial: {stock}")

def insertar_producto(nombre, precio, stock):
    """Inserta un nuevo producto en la tabla productos."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
        (nombre, precio, stock),
    )
    conexion.commit()
    conexion.close()

def listar_productos():
    """Devuelve una lista de todos los productos registrados en la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    
    print("\n--- Lista de Productos ---")
    if not productos:
        print("No hay productos registrados.")
        return
    else:
        for prod in productos:
            print(f"ID: {prod[0]}, Nombre: {prod[1]}, Precio: {prod[2]}, Stock: {prod[3]}")