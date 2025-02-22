import pandas as pd

pd_inventario = pd.read_csv('Ejercicios/Pandas/Ejercicio 02/inventario.csv')
df_usuarios=pd.read_csv('Ejercicios/Pandas/Ejercicio 02/usuarios.csv')

def inicio():
    print("Bienvenido a la tienda")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        iniciar_sesion()
    elif opcion == "2":
        registrarse()
    elif opcion == "3":
        print("Gracias por visitar la tienda")
    else:
        print("Opción inválida")
        inicio()
def iniciar_sesion():
    print("Iniciar sesión")
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuario in df_usuarios['usuario'].values:
        if df_usuarios.loc[df_usuarios['usuario'] == usuario, 'contrasena'].values[0] == contrasena:
            print("Inicio de sesión exitoso")
            menu()
        else:
            print("Contraseña incorrecta")
            inicio()
    else:
        print("Usuario no registrado")
        inicio()

def registrarse():
    print("Registrarse")
    usuario = input("Ingrese su usuario: ")
    if usuario in df_usuarios['usuario'].values:
        print("Usuario ya registrado")
        inicio()
    contrasena = input("Ingrese su contraseña: ")
    df_usuarios.loc[len(df_usuarios)] = [usuario, contrasena]
    df_usuarios.to_csv('Ejercicios/Pandas/Ejercicio 02/usuarios.csv', index=False)
    print("Usuario registrado")
    menu()

def menu():
    print("Menú")
    print("1. Ver inventario")
    print("2. Agregar nuevo producto")
    print("3. Ver productos disponibles")
    print("4. Actualizar stock")
    print("5. Actualizar precio")
    print("6. Eliminar producto")
    print("7. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        ver_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        ver_disponibles()
    elif opcion == "4":
        actualizar_stock()
    elif opcion == "5":
        actualizar_precio()
    elif opcion == "6":
        eliminar_producto()
    elif opcion == "7":
        print("Deseas salir del sistema(S/N)")
        respuesta = input().lower()
        if respuesta == 's':
            print("Gracias por visitar la tienda")
        else:
            menu()
    else:
        print("Opción inválida")
        menu()

def ver_inventario():
    print("Inventario")
    print(pd_inventario)
    print("1. Regresar")
    print("2. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        menu()
    elif opcion == "2":
        print("Deseas salir del sistema(S/N)")
        respuesta = input().lower()
        if respuesta == 's':
            print("Gracias por visitar la tienda")
        else:
            menu()
    else:
        print("Opción inválida")
        ver_inventario()

def agregar_producto():
    global pd_inventario
    print("Agregar producto")
    producto = input("Ingrese el nombre del producto: ")
    if producto in pd_inventario['Producto'].values:
        print("Producto ya registrado")
        menu()
    categoria = input("Ingrese la categoría del producto: ")
    stock = int(input("Ingrese el stock del producto: "))
    precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    proveedor = input("Ingrese el proveedor del producto: ")
    nuevo_producto = {
        'ID': len(pd_inventario) + 1,
        'Producto': producto,
        'Categoría': categoria,
        'Stock': stock,
        'Precio Unitario': precio_unitario,
        'Proveedor': proveedor
    }
    pd_inventario = pd.concat([pd_inventario, pd.DataFrame([nuevo_producto])], ignore_index=True)
    pd_inventario.to_csv('Ejercicios/Pandas/Ejercicio 02/inventario.csv', index=False)
    print("Producto agregado")
    print("1.Ingresar otro producto")
    print("2.Regresar al menú")
    print("3.Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        menu()
    elif opcion == "3":
        print("Deseas salir del sistema(S/N)")
        respuesta = input().lower()
        if respuesta == 's':
            print("Gracias por visitar la tienda")
        else:
            menu()
    else:
        print("Opción inválida")
        agregar_producto()

def ver_disponibles():
    print("Productos disponibles")
    print(pd_inventario.loc[pd_inventario['Stock'] > 0])
    print("1. Regresar")
    print("2. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        menu()
    elif opcion == "2":
        print("Deseas salir del sistema(S/N)")
        respuesta = input().lower()
        if respuesta == 'S':
            print("Gracias por visitar la tienda")
        else:
            menu()
    else:
        print("Opción inválida")
        ver_disponibles()

def actualizar_stock():
    print("Actualizar stock")
    producto_id = int(input("Ingrese el ID del producto: "))
    if producto_id in pd_inventario['ID'].values:
        stock = int(input("Ingrese el nuevo stock del producto: "))
        pd_inventario.loc[pd_inventario['ID'] == producto_id, 'Stock'] = stock
        pd_inventario.to_csv('Ejercicios/Pandas/Ejercicio 02/inventario.csv', index=False)
        print("Stock actualizado")
        print("1. Actualizar otro producto")
        print("2. Regresar al menú")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            actualizar_stock()
        elif opcion == "2":
            menu()
        elif opcion == "3":
            print("Deseas salir del sistema(S/N)")
            respuesta = input().lower()
            if respuesta == 's':
                print("Gracias por visitar la tienda")
            else:
                menu()
        else:
            print("Opción inválida")
            actualizar_stock()
    else:
        print("Producto no encontrado")
        actualizar_stock()

def actualizar_precio():
    print("Actualizar precio")
    producto_id = int(input("Ingrese el ID del producto: "))
    if producto_id in pd_inventario['ID'].values:
        precio = float(input("Ingrese el nuevo precio del producto: "))
        pd_inventario.loc[pd_inventario['ID'] == producto_id, 'Precio Unitario'] = precio
        pd_inventario.to_csv('Ejercicios/Pandas/Ejercicio 02/inventario.csv', index=False)
        print("Precio actualizado")
        print("1. Actualizar otro producto")
        print("2. Regresar al menú")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            actualizar_precio()
        elif opcion == "2":
            menu()
        elif opcion == "3":
            print("Deseas salir del sistema(S/N)")
            respuesta = input().lower()
            if respuesta == 's':
                print("Gracias por visitar la tienda")
            else:
                menu()
        else:
            print("Opción inválida")
            actualizar_precio()

def eliminar_producto():
    global pd_inventario
    print("Eliminar producto")
    producto_id = int(input("Ingrese el ID del producto: "))
    if producto_id in pd_inventario['ID'].values:
        pd_inventario = pd_inventario[pd_inventario['ID'] != producto_id]
        pd_inventario.to_csv('Ejercicios/Pandas/Ejercicio 02/inventario.csv', index=False)
        print("Producto eliminado")
        print("1. Eliminar otro producto")
        print("2. Regresar al menú")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            eliminar_producto()
        elif opcion == "2":
            menu()
        elif opcion == "3":
            print("Deseas salir del sistema(S/N)")
            respuesta = input().lower()
            if respuesta == 's':
                print("Gracias por visitar la tienda")
            else:
                menu()
        else:
            print("Opción inválida")
            eliminar_producto()
    else:
        print("Producto no encontrado")
        eliminar_producto()
inicio()