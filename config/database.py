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