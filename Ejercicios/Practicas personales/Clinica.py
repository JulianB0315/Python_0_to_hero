pacientes = []

while True:
    print("Menu de Opciones")
    print("1. Insertar paciente")
    print("2. Buscar paciente")
    print("3. Calcular costo")
    print("4. Eliminar paciente")
    print("5. Salir")
    opc = input("Seleccione una opción (1-5):\n")
    if opc not in ['1', '2', '3', '4', '5']:
        print("Opción no válida. Intenta de nuevo.")
        continue
    if opc == '1':  
        dni = input("Ingresar número de DNI del paciente: ")
        while len(dni) != 8 or not dni.isdigit():
            print("Error: El DNI solo puede tener 8 dígitos y debe ser numérico.")
            dni = input("Ingresar nuevamente el DNI del paciente: ")

        apelPart = input("Ingrese apellido paterno: ")
        apelMart = input("Ingrese apellido materno: ")
        nom = input("Ingrese nombres: ")
        edad = input("Ingrese edad del paciente: ")
        tel = input("Ingresar teléfono del paciente: ")
        cos = 100 
        informacion_paciente = [dni, apelPart, apelMart, nom, edad, tel, cos]
        pacientes.append(informacion_paciente)
        print("Información guardada correctamente.")
    elif opc == '2':  
        dni_buscar = input("Ingrese el DNI del paciente a buscar: ")
        encontrado = False
        for paciente in pacientes:
            if paciente[0] == dni_buscar:
                print("Paciente encontrado: ")
                print(f"Nombres: {paciente[3]}")
                print(f"Apellidos: {paciente[1]} {paciente[2]}")
                print(f"Edad: {paciente[4]}")
                print(f"Telfono: {paciente[5]}")
                encontrado = True
                break
        if not encontrado:
            print("Paciente no encontrado.")
    elif opc == '3':  
        dni_buscar = input("Ingrese el DNI del paciente para calcular el costo: ")
        encontrado = False
        for paciente in pacientes:
            if paciente[0] == dni_buscar:
                print(f"El costo del paciente con DNI {dni_buscar} es: {paciente[6]}") 
                encontrado = True
                break
        if not encontrado:
            print("Paciente no encontrado.")
    elif opc == '4':  
        dni_eliminar = input("Ingrese el DNI del paciente a eliminar: ")
        encontrado = False
        for paciente in pacientes:
            if paciente[0] == dni_eliminar:
                pacientes.remove(paciente)
                print(f"Paciente con DNI {dni_eliminar} ha sido eliminado.")
                encontrado = True
                break
        if not encontrado:
            print("Paciente no encontrado para eliminar.")
    elif opc == '5':  
        print("Saliendo del sistema...")
        break