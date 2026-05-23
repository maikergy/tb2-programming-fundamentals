# Archivo: config/database.py
import sqlite3

DB_FILE = "eliordas.db"


def conectar():
    """Devuelve una conexión SQLite a la base de datos."""
    return sqlite3.connect(DB_FILE)

def crear_tablas():
    """Crea las tablas necesarias si no existen."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto_id INTEGER NOT NULL,
            cantidad INTEGER NOT NULL,
            total REAL NOT NULL,
            fecha TEXT NOT NULL,
            FOREIGN KEY(producto_id) REFERENCES productos(id)
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            cargo TEXT NOT NULL,
            sueldo REAL NOT NULL
        )
        """
    )
    conexion.commit()
    conexion.close()

def insertar_data_producto():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.executemany(
    "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
    [
        ("Arroz", 4.50, 20),
        ("Azúcar", 3.20, 15),
        ("Leche", 5.00, 30),
        ("Pan", 0.50, 50),
        ("Huevos", 8.00, 25),
        ("Jabón", 2.00, 40),
        ("Shampoo", 12.50, 10),
        ("Papel Higiénico", 6.00, 18),
        ("Aceite", 9.80, 12),
        ("Gaseosa", 3.50, 22),
        ("Fideos", 2.20, 35),
        ("Café", 15.00, 8),
        ("Té", 7.50, 14),
        ("Mantequilla", 6.70, 16),
        ("Queso", 11.00, 9),
        ("Yogurt", 4.80, 13),
        ("Atún", 5.60, 17),
        ("Galletas", 2.90, 28),
        ("Chocolate", 3.40, 19),
        ("Agua", 1.50, 60),
    ])
    conexion.commit()
    conexion.close()

# QUERYS PRODUCTOS
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

def actualizar_stock_producto(id, nuevo_stock):
    """Actualiza el stock de un producto específico."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE productos SET stock = ? WHERE id = ?",
        (nuevo_stock, id),
    )
    conexion.commit()
    conexion.close()

def obtener_productos():
    """Devuelve una lista de todos los productos registrados en la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    return productos

def obtener_producto_por_nombre(nombre):
    """Busca un producto por su nombre y devuelve sus detalles."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
    producto = cursor.fetchone()
    conexion.close()
    return producto

def obtener_producto_por_id(producto_id):
    """Busca un producto por su ID."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, precio, stock FROM productos WHERE id = ?", (producto_id,))
    producto = cursor.fetchone()
    conexion.close()
    return producto

def obtener_productos_disponibles():
    """Lista los productos con stock mayor a cero."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, precio, stock FROM productos WHERE stock > 0")
    productos = cursor.fetchall()
    conexion.close()
    return productos


# QUERYS VENTAS
def obtener_ventas():
    """Muestra el historial de ventas guardado en la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT p.nombre, v.cantidad, v.total, v.fecha"
        " FROM ventas v"
        " JOIN productos p ON v.producto_id = p.id"
        " ORDER BY v.fecha DESC, v.id DESC"
    )
    ventas = cursor.fetchall()
    conexion.close()
    return ventas

def insertar_venta_y_actualizar_stock(producto_id, cantidad, total, fecha):
    """Inserta una nueva venta en la tabla ventas."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO ventas (producto_id, cantidad, total, fecha) VALUES (?, ?, ?, ?)",
        (producto_id, cantidad, total, fecha),
    )
    cursor.execute(
        "UPDATE productos SET stock = stock - ? WHERE id = ?",
        (cantidad, producto_id),
    )
    conexion.commit()
    conexion.close()

# QUERYS NOMINA
def insertar_empleado(nombre, cargo, sueldo):
    """Inserta un nuevo empleado en la tabla empleados."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO empleados (nombre, cargo, sueldo) VALUES (?, ?, ?)",
        (nombre, cargo, sueldo),
    )
    conexion.commit()
    conexion.close()

def obtener_empleado_por_nombre(nombre):
    """Busca un empleado por su nombre y devuelve sus detalles."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM empleados WHERE LOWER(nombre) = LOWER(?)", (nombre,))
    empleado = cursor.fetchone()
    conexion.close()
    return empleado

def obtener_empleados():
    """Devuelve una lista de todos los empleados registrados en la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    conexion.close()
    return empleados