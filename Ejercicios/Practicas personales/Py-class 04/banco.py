import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Cargar los datos directamente
df_cuentas = pd.read_excel('Ejercicios/Practicas personales/Py-class 04/Cuentas.xlsx', dtype={'DNI': str, 'Contraseña': str, 'Saldo': float})
df_transacciones = pd.read_excel('Ejercicios/Practicas personales/Py-class 04/Transacciones.xlsx', dtype={'DNI': str, 'Monto': float})

class Cuenta:
    def __init__(self, dni, apelPart, apelMart, nom, edad, contra, saldo=0.0):
        self.dni = dni
        self.apelPart = apelPart
        self.apelMart = apelMart
        self.nom = nom
        self.edad = edad
        self.contra = contra
        self.saldo = saldo

def crearCuenta():
    global df_cuentas
    dni = input("Ingresar número de DNI del titular: \n")
    while len(dni) != 8 or not dni.isdigit():
        print("Error: El DNI solo puede tener 8 dígitos y debe ser numérico.")
        dni = input("Ingresar nuevamente el DNI del titular: \n")
    
    apelPart = input("Ingrese apellido paterno: \n")
    apelMart = input("Ingrese apellido materno: \n")
    nom = input("Ingrese nombres: \n")
    edad = int(input("Ingrese edad del titular: \n"))
    while edad < 18:
        print("El titular debe de ser mayor de edad")
        edad = int(input("Ingresar nuevamente la edad del titular: \n"))

    contra = input("Ingresar contraseña (8 dígitos): \n")
    while len(contra) != 8 or not contra.isdigit():
        print("Error: La contraseña debe tener 8 dígitos numéricos.")
        contra = input("Ingresar nuevamente la contraseña (8 dígitos): \n")

    cuenta = Cuenta(dni, apelPart, apelMart, nom, edad, contra)
    df_nueva_cuenta = pd.DataFrame({'DNI': [dni], 'Apellido Paterno': [apelPart], 'Apellido Materno': [apelMart], 'Nombre': [nom], 'Edad': [edad], 'Contraseña': [contra], 'Saldo': [cuenta.saldo]}) 
    df_cuentas = pd.concat([df_cuentas, df_nueva_cuenta], ignore_index=True)
    df_cuentas.to_excel('Ejercicios/Practicas personales/Py-class 04/Cuentas.xlsx', sheet_name='Cuentas', index=False)
    print("---------------------------------------")
    print("--Información guardada correctamente.--")
    print("---------------------------------------\n")

def retirarDinero():
    global df_cuentas, df_transacciones
    dni = input("Ingresar número de DNI del titular: \n")
    while len(dni) != 8 or not dni.isdigit():
        print("Error: El DNI solo puede tener 8 dígitos y debe ser numérico.")
        dni = input("Ingresar nuevamente el DNI del titular: \n")
    
    cuenta_encontrada = df_cuentas[df_cuentas['DNI'] == dni]
    if not cuenta_encontrada.empty:
        contra = input("Ingresar la contraseña: \n")
        if contra == cuenta_encontrada.iloc[0]['Contraseña']:
            cantidad = float(input("¿Cuánto dinero desea retirar?: \n"))
            saldo_actual = cuenta_encontrada.iloc[0]['Saldo']
            if cantidad > saldo_actual:
                print("Saldo insuficiente.")
                return
            saldo_actual -= cantidad
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
            print("**********************")
            print("**Retiro realizado**")
            print(f"N° DNI: {dni}")
            print(f"Monto retiro: s/.{cantidad}")
            print(f"Saldo actual: s/.{saldo_actual}")
            print(f"Fecha de retiro: {fecha}")
            print("**********************\n")
            # Guardar transacción
            df_transacciones = pd.concat([df_transacciones, pd.DataFrame({'DNI': [dni], 'Tipo': ['Retiro'], 'Monto': [cantidad], 'Fecha': [fecha]})], ignore_index=True)
            df_transacciones.to_excel('Ejercicios/Practicas personales/Py-class 04/Transacciones.xlsx', sheet_name='Transacciones', index=False)
            df_cuentas.loc[df_cuentas['DNI'] == dni, 'Saldo'] = saldo_actual
            df_cuentas.to_excel('Ejercicios/Practicas personales/Py-class 04/Cuentas.xlsx', sheet_name='Cuentas', index=False)
        else:
            print("Contraseña incorrecta.")
    else:
        print("Cuenta no encontrada.")

def ingresarDinero():
    global df_cuentas, df_transacciones
    dni = input("Ingresar número de DNI del titular: \n")
    while len(dni) != 8 or not dni.isdigit():
        print("Error: El DNI solo puede tener 8 dígitos y debe ser numérico.")
        dni = input("Ingresar nuevamente el DNI del titular: \n")
    
    cuenta_encontrada = df_cuentas[df_cuentas['DNI'] == dni]
    if not cuenta_encontrada.empty:
        contra = input("Ingresar la contraseña: \n")
        if contra == cuenta_encontrada.iloc[0]['Contraseña']:
            cantidad = float(input("¿Cuánto dinero desea ingresar?: \n"))
            saldo_actual = cuenta_encontrada.iloc[0]['Saldo']
            saldo_actual += cantidad
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
            print("**********************")
            print("**Depósito realizado**")
            print(f"N° DNI: {dni}")
            print(f"Monto depósito: s/.{cantidad}")
            print(f"Saldo actual: s/.{saldo_actual}")
            print(f"Fecha de depósito: {fecha}")
            print("**********************\n")
            df_transacciones = pd.concat([df_transacciones, pd.DataFrame({'DNI': [dni], 'Tipo': ['Deposito'], 'Monto': [cantidad], 'Fecha': [fecha]})], ignore_index=True)
            df_transacciones.to_excel('Ejercicios/Practicas personales/Py-class 04/Transacciones.xlsx', sheet_name='Transacciones', index=False)
            df_cuentas.loc[df_cuentas['DNI'] == dni, 'Saldo'] = saldo_actual
            df_cuentas.to_excel('Ejercicios/Practicas personales/Py-class 04/Cuentas.xlsx', sheet_name='Cuentas', index=False)
        else:
            print("Contraseña incorrecta.")
    else:
        print("Cuenta no encontrada.")

def revisarEstado():
    global df_cuentas
    dni = input("Ingresar número de DNI del titular:\n ")
    while len(dni) != 8 or not dni.isdigit():
        print("Error: El DNI solo puede tener 8 dígitos y debe ser numérico.")
        dni = input("Ingresar nuevamente el DNI del titular: \n")

    cuenta_encontrada = df_cuentas[df_cuentas['DNI'] == dni]
    if not cuenta_encontrada.empty:
        contra = input("Ingresar la contraseña: \n")
        if contra == cuenta_encontrada.iloc[0]['Contraseña']:
            print("**********************")
            print(f"N° DNI del titular: {dni}")
            print(f"Titular: {cuenta_encontrada.iloc[0]['Nombre']} {cuenta_encontrada.iloc[0]['Apellido Paterno']} {cuenta_encontrada.iloc[0]['Apellido Materno']}")
            print(f"Saldo actual: s/.{cuenta_encontrada.iloc[0]['Saldo']}")
            print("**********************\n")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Cuenta no encontrada.")

def mostrar_grafica_transacciones():
    global df_transacciones
    
    dni = input("Ingresar número de DNI del titular para filtrar transacciones: \n")
    while len(dni) != 8 or not dni.isdigit():
        print("Error: El DNI solo puede tener 8 dígitos y debe ser numérico.")
        dni = input("Ingresar nuevamente el DNI del titular: \n")
    
    transacciones_filtradas = df_transacciones[df_transacciones['DNI'] == dni]
    
    if transacciones_filtradas.empty:
        print("No se encontraron transacciones para el DNI proporcionado.")
        return
    
    transacciones_tipo = transacciones_filtradas['Tipo'].value_counts()
    
    labels = transacciones_tipo.index
    sizes = transacciones_tipo.values
    colors = ['#ff9999','#66b3ff']

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title(f'Distribución de Transacciones')
    plt.show()

def estadicticas():
    global df_cuentas, df_transacciones
    print("Estadísticas Generales del Banco")
    print("********************************")
    print(f"Total de cuentas registradas: {df_cuentas.shape[0]}")
    print(f"Total de transacciones realizadas: {df_transacciones.shape[0]}")
    print(f"Total de depósitos realizados en el banco: {df_transacciones[df_transacciones['Tipo'] == 'Deposito'].shape[0]}")
    print(f"Total de retiros realizados en el banco: {df_transacciones[df_transacciones['Tipo'] == 'Retiro'].shape[0]}")
    print("********************************\n")
    # Gráfico de torta de transacciones por tipo
    transacciones_tipo = df_transacciones['Tipo'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(transacciones_tipo, labels=transacciones_tipo.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], startangle=140)
    plt.title('Distribución de Transacciones por Tipo')
    plt.axis('equal')
    plt.show()

    # Gráfico de torta de distribución de saldos
    top_5_cuentas = df_cuentas.nlargest(5, 'Saldo')
    plt.figure(figsize=(10, 6))
    plt.bar(top_5_cuentas['Nombre'], top_5_cuentas['Saldo'], color='skyblue')
    plt.xlabel('Nombre del Titular')
    plt.ylabel('Saldo')
    plt.title('Top 5 Cuentas con Mayor Saldo')
    plt.xticks(rotation=45)
    plt.show()

    # Gráfico de línea de saldo a lo largo del tiempo para un DNI específico
    dni = input("Ingresar número de DNI del titular para ver la evolución del saldo: \n")
    while len(dni) != 8 or not dni.isdigit():
        print("Error: El DNI solo puede tener 8 dígitos y debe ser numérico.")
        dni = input("Ingresar nuevamente el DNI del titular: \n")
    
    transacciones_dni = df_transacciones[df_transacciones['DNI'] == dni]
    if transacciones_dni.empty:
        print("No se encontraron transacciones para el DNI proporcionado.")
        return
    
    transacciones_dni['Fecha'] = pd.to_datetime(transacciones_dni['Fecha'])
    transacciones_dni = transacciones_dni.sort_values(by='Fecha')
    transacciones_dni['Saldo'] = transacciones_dni['Monto'].cumsum()
    
    plt.figure(figsize=(10, 6))
    plt.plot(transacciones_dni['Fecha'], transacciones_dni['Saldo'], marker='o')
    plt.title(f'Evolución del Saldo para DNI: {dni}')
    plt.xlabel('Fecha')
    plt.ylabel('Saldo')
    plt.grid(True)
    plt.show()

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
        print("5 -> Mostrar gráfica de transacciones")
        print("*****************************************")
        print("6 -> Generales del banco")
        print("*****************************************")
        print("7 -> Salir")
        print("*****************************************\n")
        
        opc = input("Ingrese número de acción que desea hacer: \n")
        if opc not in ["1", "2", "3", "4", "5", "6", "7"]:
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
            mostrar_grafica_transacciones()
        elif opc == "6":
            estadicticas()
        elif opc == "7":
            salir = input("Deseas salir del cajero (si/no)").strip().lower()
            if salir == "si":
                print("Gracias por su visita, regrese pronto.")
                break
            else:
                print("Sigamos trabajando.")
                continue

if __name__ == "__main__":
    menu()