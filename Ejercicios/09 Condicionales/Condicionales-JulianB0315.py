## **Ejercicio 1: Determinar si puedes aprender a conducir**
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres lo suficiente mayor para aprender a conducir")
else:
    edad_faltante= 18 - edad
    print(f"Necesitas {edad_faltante} años más para aprender a conducir")

## **Ejercicio 2: Comparar edades**
mi_edad = 20
usuario_edad = int(input("Ingrese la edad del usuario: "))
if mi_edad > usuario_edad:
    print(f"Soy {mi_edad-usuario_edad} años mayor que tú")
elif mi_edad < usuario_edad:
    print(f"Eres {usuario_edad-mi_edad} años mayor que yo")
else:
    print("Tenemos la misma edad")
## **Ejercicio 3: Comparar dos números**
a= int(input("Ingrese el valor de a: "))
b= int(input("Ingrese el valor de b: "))
if a > b:
    print("a es mayor que b")
elif a < b:
    print("b es mayor que a")
else:
    print("a es igual a b")

## **Ejercicio 4: Calificar estudiantes según sus notas**
nota = int(input("Ingrese la nota del estudiante, mayor a 0 menor de 100: "))
if nota >= 80 and nota <= 100:
    print("A")
elif nota >= 70 and nota < 80:
    print("B")
elif nota >= 60 and nota < 70:
    print("C")
elif nota >= 50 and nota < 60:
    print("D")
elif nota >= 0 and nota < 50:
    print("F")
else:
    print("Nota no válida")

## **Ejercicio 5: Determinar la estación del año**
mes = input("Ingrese el mes en el que se encuentra: ")
meses_verano = ["junio", "julio", "agosto"]
meses_otono = ["septiembre", "octubre", "noviembre"]
meses_invierno = ["diciembre", "enero", "febrero"]
meses_primavera = ["marzo", "abril", "mayo"]
if mes in meses_verano:
    print("Verano")
elif mes in meses_otono:
    print("Otoño")
elif mes in meses_invierno:
    print("Invierno")
elif mes in meses_primavera:
    print("Primavera")
else:
    print("Mes no válido")
    
## **Ejercicio 6: Lista de frutas**
frutas = ['banana', 'naranja', 'mango', 'limón']
fruta = input("Ingrese una fruta: ")
if fruta in frutas:
    print("La fruta está en la lista")
else:
    frutas.append(fruta)
    print("La fruta no está en la lista, se ha añadido a la lista")
    print(frutas)
    
## **Ejercicio 7: Trabajando con diccionarios**
persona = {
    'nombre': 'Juan',
    'apellido': 'Pérez',
    'edad': 30,
    'país': 'España',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'dirección': {
        'calle': 'Calle Luna',
        'código_postal': '28001'
    }
}
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    print("Su habilidades son: ", habilidades[len(habilidades) // 2])
else:
    print("No tiene habilidades")

#Buscar python
if 'Python' in persona['habilidades']:
    print("Python está en sus habilidades")
else:
    print("Python no está en sus habilidades")

#Evaluar habilidades
if set(persona['habilidades']) == {"JavaScript", "React"}:
    print("Es un desarrollador frontend.")
elif set(persona['habilidades']) == {"Node","Python", "MongoDB"}:
    print("Es un desarrollador backend.")
elif set(persona['habilidades']) == { "React", "Node", "MongoDB"}:
    print("Es un desarrollador fullstack.")
else:
    print("Titulo desconocido")

#Evaluar estado civil y país
if persona['casado'] and persona['país'] == 'España':
    print("Nombre ;",persona['nombre'], persona['apellido'])
    print("País ;",persona['país'])
    if persona['casado']:
        print("Estado civil ; Casado")
    else:
        print("Estado civil ; Soltero")