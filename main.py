from config.database import crear_tablas, insertar_data_producto
from modules.inventario import modulo_inventario
from modules.ventas import modulo_ventas
from modules.reportes import modulo_reportes
from modules.nomina import modulo_nomina

def menu_principal():
    """Muestra el menú principal interactivo."""
    while True:
        print("\n=== ELIORODAS - Menú Principal ===")
        print("1. Inventario")
        print("2. Ventas")
        print("3. Reportes")
        print("4. Nómina")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            modulo_inventario()
        elif opcion == "2":
            modulo_ventas()
        elif opcion == "3":
            modulo_reportes()
        elif opcion == "4":
            modulo_nomina()
        elif opcion == "5":
            print("Saliendo del sistema. Hasta pronto.")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")


if __name__ == "__main__":
    crear_tablas()
    insertar_data_producto()
    menu_principal()