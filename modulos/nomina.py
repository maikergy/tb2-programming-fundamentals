empleados = []

def registrar_empleado():

    nombre = input("Nombre: ")
    cargo = input("Cargo: ")
    sueldo = float(input("Sueldo: "))

    empleado = {
        "nombre": nombre,
        "cargo": cargo,
        "sueldo": sueldo
    }

    empleados.append(empleado)

    print("Empleado registrado correctamente")


def calcular_salario():

    nombre = input("Ingrese nombre del empleado: ")

    for empleado in empleados:

        if empleado["nombre"] == nombre:

            bono = float(input("Bono: "))
            descuento = float(input("Descuento: "))

            salario = empleado["sueldo"] + bono - descuento

            print("Salario neto:", salario)
            return

    print("Empleado no encontrado")


def ver_nomina():

    if len(empleados) == 0:
        print("No hay empleados registrados")

    else:
        for empleado in empleados:
            print("----------------")
            print("Nombre:", empleado["nombre"])
            print("Cargo:", empleado["cargo"])
            print("Sueldo:", empleado["sueldo"])


def modulo_nomina():

    while True:

        print("\n--- MÓDULO NÓMINA ---")
        print("1. Registrar Empleado")
        print("2. Calcular Salario")
        print("3. Ver Nómina")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_empleado()

        elif opcion == "2":
            calcular_salario()

        elif opcion == "3":
            ver_nomina()

        elif opcion == "4":
            break

        else:
            print("Opción inválida")