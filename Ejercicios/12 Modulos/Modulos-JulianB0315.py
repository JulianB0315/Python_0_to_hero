#Ejercicio 1:
def generar_id_usuario():
    import random
    import string
    longitud = 6
    valores = string.ascii_letters + string.digits 
    p = ''.join(random.choice(valores) for i in range(longitud))
    return p
print(generar_id_usuario())

#Ejercicio 2:
def generar_ids_por_usuario(longitud,cantidad):
    import random
    import string
    valores = string.ascii_letters + string.digits
    for i in range(cantidad):
        p = ''.join(random.choice(valores) for i in range(longitud))
        print(p)
cantidad = int(input("Ingrese la cantidad de id's que desea generar: "))
longitud = int(input("Ingrese la longitud de los id's: "))
generar_ids_por_usuario(longitud,cantidad)

#Ejercicio 3:
def generar_color_rgb():
    import random
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
print(generar_color_rgb())

#Ejercicio 4:
def lista_colores_hexadecimales(cantidad):
    import random
    lista = []
    for i in range(cantidad):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        lista.append(f"#{r:02x}{g:02x}{b:02x}")
    return lista
cantidad = int(input("Ingrese la cantidad de colores hexadecimales que desea generar: "))
print(lista_colores_hexadecimales(cantidad))

#Ejercicio 5:
def lista_colores_rgb(cantidad):
    import random
    lista = []
    for i in range(cantidad):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        lista.append((r,g,b))
    return lista
cantidad = int(input("Ingrese la cantidad de colores RGB que desea generar: "))
print(lista_colores_rgb(cantidad))

#Ejercicio 6:
def generar_colores(tipo,cantidad):
    if tipo == "RGB":
        return lista_colores_rgb(cantidad)
    elif tipo == "HEXA":
        return lista_colores_hexadecimales(cantidad)
    else:
        return "Tipo de color no soportado"
tipo = input("Ingrese el tipo de color que desea generar (RGB/HEXA): ")
cantidad = int(input("Ingrese la cantidad de colores que desea generar: "))
print(generar_colores(tipo,cantidad))
