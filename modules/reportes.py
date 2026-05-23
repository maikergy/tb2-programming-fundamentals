# Archivo: modules/reportes.py
from datetime import datetime
from config.database import conectar

def modulo_reportes():
    """Muestra el submenú del módulo de reportes."""
    while True:
        print("\n--- Módulo Reporte Diario ---")
        print("1. Mostrar Reporte Diario")
        print("2. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            generar_reporte_diario()
        elif opcion == "2":
            return
        else:
            print("Opción inválida. Intente de nuevo.")

def generar_reporte_diario():
    """Genera el reporte de ventas del día actual."""
    hoy = datetime.now().strftime("%Y-%m-%d")
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT COUNT(*), COALESCE(SUM(total), 0), COALESCE(SUM(cantidad), 0)"
        " FROM ventas WHERE fecha = ?",
        (hoy,),
    )
    total_ventas, monto_total, productos_vendidos = cursor.fetchone()
    conexion.close()

    print("\n--- Reporte Diario ---")
    print(f"Fecha: {hoy}")
    print(f"Ventas registradas: {total_ventas}")
    print(f"Total facturado: {monto_total}")
    print(f"Productos vendidos: {productos_vendidos}")