from datetime import datetime

Cuentas = []

class Cuenta:
    def __init__(self, dni, apelPart, apelMart, nom, edad, contra):
        self.dni = dni
        self.apelPart = apelPart
        self.apelMart = apelMart
        self.nom = nom
        self.edad = edad
        self.contra = contra
        self.saldo = 0  

    def ingresar_dinero(self, cantidad):
        self.saldo += cantidad
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        print("**********************")
        print("**Deposito relizado**")
        print(f"N° DNI: {self.dni}")
        print(f"Monto deposito: s/.{cantidad}")
        print(f"Saldo actual: s/.{self.saldo}")
        print(f"Fecha de deposito:{fecha}")
        print("**********************\n")

    def retirar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

            print("**********************")
            print("**Retiro relizado**")
            print(f"N° DNI: {self.dni}")
            print(f"Monto retirado: s/.{cantidad}")
            print(f"Saldo actual: s./{self.saldo}")
            print(f"Fecha de retiro: {fecha}")
            print("**********************\n")
        else:
            print("Saldo insuficiente.")

    def revisar_estado(self):
        print("**********************")
        print(f"N° DNI del titular: {self.dni}")
        print(f"Titular: {self.apelPart} {self.apelMart} {self.nom}")
        print(f"Saldo actual: {self.saldo}")
        print("**********************\n")

def crearCuenta():
    dni = input("Ingresar número de DNI del titular: \n")
    while len(dni) != 8 or not dni.isdigit():
        print("Error: El DNI solo puede tener 8 dígitos y debe ser numérico.")
        dni = input("Ingresar nuevamente el DNI del titular: \n")
    
    apelPart = input("Ingrese apellido paterno: \n")
    apelMart = input("Ingrese apellido materno: \n")
    nom = input("Ingrese nombres: \n")
    edad = int(input("Ingrese edad del titular: \n"))
    while edad<18 :
        print("El titular debe de ser mayor de edad")
        edad = int(input("Ingresar nuevamente la edad del titular: \n"))

    contra = input("Ingresar contraseña (8 dígitos): \n")
    while len(contra) != 8 or not contra.isdigit():
        print("Error: La contraseña debe tener 8 dígitos numéricos.")
        contra = input("Ingresar nuevamente la contraseña (8 dígitos): \n")

    cuenta = Cuenta(dni, apelPart, apelMart, nom, edad, contra)
    Cuentas.append(cuenta)
    print("---------------------------------------")
    print("--Información guardada correctamente.--")
    print("---------------------------------------\n")


def retirarDinero():
    dni = input("Ingresar número de DNI del titular: \n")
    while len(dni) != 8 or not dni.isdigit():
        print("Error: El DNI solo puede tener 8 dígitos y debe ser numérico.")
        dni = input("Ingresar nuevamente el DNI del titular: \n")
    
    cuenta_encontrada = None
    for cuenta in Cuentas:
        if cuenta.dni == dni:
            cuenta_encontrada = cuenta
            break

    if cuenta_encontrada:
        contra = input("Ingresar la contraseña: \n")
        if contra == cuenta_encontrada.contra:
            cantidad = float(input("¿Cuánto dinero desea retirar?: \n"))
            cuenta_encontrada.retirar_dinero(cantidad)
        else:
            print("Contraseña incorrecta.")
    else:
        print("Cuenta no encontrada.")

def ingresarDinero():
    dni = input("Ingresar número de DNI del titular: \n")
    while len(dni) != 8 or not dni.isdigit():
        print("Error: El DNI solo puede tener 8 dígitos y debe ser numérico.")
        dni = input("Ingresar nuevamente el DNI del titular: \n")

    cuenta_encontrada = None
    for cuenta in Cuentas:
        if cuenta.dni == dni:
            cuenta_encontrada = cuenta
            break

    if cuenta_encontrada:
        contra = input("Ingresar la contraseña: \n")
        if contra == cuenta_encontrada.contra:
            cantidad = float(input("¿Cuánto dinero desea ingresar?: \n"))
            cuenta_encontrada.ingresar_dinero(cantidad)
        else:
            print("Contraseña incorrecta.")
    else:
        print("Cuenta no encontrada.")

def revisarEstado():
    dni = input("Ingresar número de DNI del titular:\n ")
    while len(dni) != 8 or not dni.isdigit():
        print("Error: El DNI solo puede tener 8 dígitos y debe ser numérico.")
        dni = input("Ingresar nuevamente el DNI del titular: \n")

    cuenta_encontrada = None
    for cuenta in Cuentas:
        if cuenta.dni == dni:
            cuenta_encontrada = cuenta
            break

    if cuenta_encontrada:
        contra = input("Ingresar la contraseña: \n")
        if contra == cuenta_encontrada.contra:
            cuenta_encontrada.revisar_estado()
        else:
            print("Contraseña incorrecta.")
    else:
        print("Cuenta no encontrada.")

def menu():
    while True:
        print("**** Bienvenido al cajero automático ****")
        print("*****************************************")
        print("Por favor seleccione lo que desea hacer:")
        print("*****************************************")
        print("1 -> Abrir una nueva cuenta")
        print("*****************************************")
        print("2 -> Retirar dinero")
        print("*****************************************")
        print("3 -> Ingresar dinero")
        print("*****************************************")
        print("4 -> Revisar estado de cuenta")
        print("*****************************************")
        print("5 -> Salir del sistema")
        print("*****************************************\n")
        
        opc = input("Ingrese número de acción que desea hacer: \n")
        if opc not in ["1", "2", "3", "4", "5"]:
            print("Opción no válida. Intente de nuevo.")
            continue

        if opc == "1":
            crearCuenta()
        elif opc == "2":
            retirarDinero()
        elif opc == "3":
            ingresarDinero()
        elif opc == "4":
            revisarEstado()
        elif opc == "5":
            salir=input("Deseas salir del cajero (si/no)").strip().lower()
            if salir=="si":
                print("Gracias por su visita,regrese pronto.")
                break
            else:
                print("Sigamos trabajando.")
                continue
if __name__ == "__main__":
    menu()