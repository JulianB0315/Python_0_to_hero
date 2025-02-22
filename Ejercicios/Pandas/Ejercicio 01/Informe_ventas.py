import pandas as pd
import matplotlib.pyplot as plt

df_ventas=pd.read_csv('Ejercicios/Pandas/Ejercicio 01/ventas.csv')
df_usuarios=pd.read_csv('Ejercicios/Pandas/Ejercicio 01/usuarios.csv')

def inicio():
    print("Bienvenido al sistema de ventas")
    print("Ingresar usuario y contraseña")
    usuario=input("Usuario: ")
    contraseña=input("Contraseña: ")
    if usuario in df_usuarios['usuario'].values:
        if df_usuarios[df_usuarios['usuario']==usuario]['contrasena'].values[0]==contraseña:
            print("Usuario autenticado")
            menu()
        else:
            print("Contraseña incorrecta")
            inicio()
    else:
        print("Usuario no existe")
        inicio()

def consultar_ventas():
    print("Consulta de ventas")
    print(df_ventas)
    print("Siguiente consulta")
    print("1. Mostrar grafica de ventas por categoría")
    print("2. Mostrar grafica de ventas por producto")
    print("3. Regresar al menú principal")
    menu_consultar_ventas()

def menu_consultar_ventas():
    opcion=input("Ingrese una opción: ")
    if opcion=='1':
        df_ventas.groupby('Categoría').sum().reset_index().plot(kind='bar', x='Categoría', y='Total')
        plt.show()
        menu_consultar_ventas()
    elif opcion=='2':
        df_ventas.groupby('Producto')['Total'].sum().reset_index().plot(kind='bar', x='Producto', y='Total')
        plt.show()
        menu_consultar_ventas()
    elif opcion=='3':
        menu()
    else:
        print("Opción incorrecta")
        menu_consultar_ventas()

def consultar_ventas_producto():
    print("Consulta de ventas por producto")
    producto=input("Ingrese el nombre del producto: ")
    print(df_ventas[df_ventas['Producto']==producto])
    print("Siguiente consulta")
    print("1. Mostrar grafica de ventas por producto")
    print("2. Regresar al menú principal")
    opcion=input("Ingrese una opción: ")
    if opcion=='1':
        df_ventas[df_ventas['Producto']==producto].groupby('Producto').sum().plot(kind='bar')
        plt.show()
        menu()
    elif opcion=='2':
        menu()
    else:
        print("Opción incorrecta")
        menu()

def consultar_ventas_categoria():
    print("Consulta de ventas por categoría")
    categoria=input("Ingrese el nombre de la categoría: ")
    print(df_ventas[df_ventas['Categoría']==categoria])
    print("Siguiente consulta")
    print("1. Mostrar grafica de ventas por categoría")
    print("2. Regresar al menú principal")
    opcion=input("Ingrese una opción: ")
    if opcion=='1':
        df_ventas[df_ventas['Categoría']==categoria].groupby('Categoría').sum().plot(kind='bar')
        plt.show()
        menu()
    elif opcion=='2':
        menu()
    else:
        print("Opción incorrecta")
        menu()

def consultar_ventas_fecha():
    print("Consulta de ventas por fecha")
    fecha=input("Ingrese la fecha (yyyy-mm-dd): ")
    print(df_ventas[df_ventas['Fecha']==fecha])
    print("Siguiente consulta")
    print("1. Mostrar grafica de ventas por fecha")
    print("2. Regresar al menú principal")
    opcion=input("Ingrese una opción: ")
    if opcion=='1':
        df_ventas[df_ventas['Fecha']==fecha].groupby('Fecha').sum().plot(kind='bar')
        plt.show()
        menu()
    elif opcion=='2':
        menu()
    else:
        print("Opción incorrecta")
        menu()

def consultar_total_ventas():
    print("Consulta de total de ventas")
    print("El total de ventas es: ",df_ventas['Total'].sum())
    print("Siguiente consulta")
    print("1. Mostrar grafica de total de ventas")
    print("2. Regresar al menú principal")
    opcion=input("Ingrese una opción: ")
    if opcion=='1':
        df_ventas.groupby('Fecha').sum().plot(kind='bar')
        plt.show()
        menu()
    elif opcion=='2':
        menu()
    else:
        print("Opción incorrecta")
        menu()

def menu():
    print("Menú de opciones")
    print("1. Consultar ventas")
    print("2. Consultar ventas por producto")
    print("3. Consultar ventas por categoría")
    print("4. Consultar ventas por fecha")
    print("5. Consultar total de ventas")
    print("6. Salir")
    opcion=input("Ingrese una opción: ")
    if opcion=='1':
        consultar_ventas()
    elif opcion=='2':
        consultar_ventas_producto()
    elif opcion=='3':
        consultar_ventas_categoria()
    elif opcion=='4':
        consultar_ventas_fecha()
    elif opcion=='5':
        consultar_total_ventas()
    elif opcion=='6':
        print("Deseas salir del sistema (si/no)")
        respuesta=input().lower()
        if respuesta=='si':
            print("Hasta luego")
        elif respuesta=='no':
            menu()
        else:
            print("Opción incorrecta")
            menu()
    else:
        print("Opción incorrecta")
        menu()  

inicio()