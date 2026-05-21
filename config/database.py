# Archivo: config/database.py
import sqlite3

DB_FILE = "eliordas.db"


def conectar():
    """Devuelve una conexión SQLite a la base de datos."""
    return sqlite3.connect(DB_FILE)

def crear_tabla_productos():
    """Crea la tabla productos si no existe."""
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
    conexion.commit()
    conexion.close()