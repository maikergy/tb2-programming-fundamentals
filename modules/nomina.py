from config.database import *

def modulo_nomina():
    """Muestra el submenú del módulo de nómina."""
    while True:
        print("\n--- MÓDULO NÓMINA ---")
        print("1. Registrar Empleado")
        print("2. Calcular Salario")
        print("3. Ver Nómina")
        print("4. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            calcular_salario()
        elif opcion == "3":
            ver_nomina()
        elif opcion == "4":
            return
        else:
            print("Opción inválida. Intente de nuevo.")


def registrar_empleado():

    nombre = input("Nombre: ")
    cargo = input("Cargo: ")

    try:
        sueldo = float(input("Sueldo: "))

    except ValueError:
        print("Sueldo inválido")
        return

    insertar_empleado(nombre, cargo, sueldo)

    print("Empleado registrado correctamente")


def calcular_salario():

    nombre = input("Ingrese nombre del empleado: ")

    empleado = obtener_empleado_por_nombre(nombre)

    if empleado:

        sueldo = empleado[0]

        bono = float(input("Bono: "))
        descuento = float(input("Descuento: "))

        salario = sueldo + bono - descuento

        print(f"Salario neto: S/. {salario:.2f}")

    else:
        print("Empleado no encontrado")


def ver_nomina():
    empleados = obtener_empleados()

    if len(empleados) == 0:
        print("No hay empleados registrados")

    else:

        for empleado in empleados:

            print(f"ID: {empleado[0]}, Nombre: {empleado[1]}, Cargo: {empleado[2]}, Sueldo: S/. {empleado[3]:.2f}")