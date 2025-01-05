#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora como acedemos a los datos de la lista, para usemos la indexación positiva
#Accedemos a cada elemento de una lista utilizando su índice. Un índice de lista comienza desde 0.
frutas = ['platano', 'naranja', 'mango', 'manzana']
#            0           1         2         3
#Sabiendo esto como llámanos los elementos de la lista
fruta_0=frutas[0]
print(fruta_0)
fruta_1=frutas[1]
print(fruta_1)
fruta_2=frutas[2]
print(fruta_2)
fruta_3=frutas[3]
print(fruta_3)
last_index = len(frutas) - 1#Cuentas los elementos de frutas y al resultado le resta 1 
last_fruta = frutas[last_index]
#-------------------------------------------------------------------------------------------------------------------------------------------
#Acceso a Elementos de Lista Usando Indexación Negativa
#Es casi lo mismo, pero usando numero negativos
#Medios de indexación negativos que comienzan desde el final, - 1 se refiere al último elemento, - 2 se refiere al segundo último elemento.
vegetales = ['Tomate', 'Papa', 'Palta','Cebolla', 'Zanahoria']
#              -5       -4        -3      -2           -1
vegetal_1=vegetales[-1]
print(vegetal_1)
vegetal_2=vegetales[-2]
print(vegetal_2)
vegetal_3=vegetales[-3]
print(vegetal_3)
vegetal_4=vegetales[-4]
print(vegetal_4)
vegetal_5=vegetales[-5]
print(vegetal_5)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Desempaquetar Artículos de la Lista
#Se crea una lista y para llamar los elementos le damos variables a cada uno
Alumnos=('Juan','Pedro','Diego','Juan','Daniel')
#Damos variables
T1,T2,T3,*restante=Alumnos#Usamos * y damos un nombre para elementos que no tienen variable dependiendo su posición
print(T1)
print(T2)
print(T3)
print(restante)
#Otros ejemplos de como desempaquetar
num=(1,2,3,4,5,6,7,8,9,10)
num1,num2,num3,num4,num5,*resnum,num9,num10=num
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(resnum)
print(num9)
print(num10)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora probemos cortando elementos de una para tomas solo los que se necesita
#Con la indexación positiva será así
#Indexación positiva: Podemos especificar un rango de índices positivos especificando el inicio
#El final y el paso, el valor de retorno será una nueva lista.
paises = ['Argentina', 'Colombia', 'Chile', 'Bolivia', 'Perú']#(valores predeterminados para el inicio = 0, final = len(lst) - 1 (último artículo), paso = 1)
todo=paises[0:5]#Al poner una limite mayor al de número de elementos (comenzando desde 0) tomamos todos
print(todo)#Devuelve todo 
todo_2=paises=paises[0:]#Al no poner un final devuelve todo 
print(todo_2)
colombia_chile=paises[1:3]#no incluye el primer índice, dando limite hasta Bolivia si incluirlo
print(colombia_chile)
salto=paises[::2]#Aquí usamos un tercer argumento,para dar un salto. Se necesitarán cada segundo artículo 
print(salto)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Y con la indexación negativa seria así
web= ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']
completa=web[-8:]# Al ser el 0 mayor que lo números negativos y al usar -1 excluimos ala último elemento de la lista, mejor no le damos limite y así retornamos todo
print(completa)
html_css=web[-7:-5]
print(html_css)
salto_2=web[::-2]
print(salto_2)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora modificamos las listas creadas
#La lista es una colección ordenada mutable o modificable de artículos. Modifiquemos la lista de vegetales.
vegetales = ['Tomate', 'Papa', 'Palta','Cebolla', 'Zanahoria']
vegetales[0]='Brocoli'#con esto indicamos que el elemento de 0 se cambia por otro
print(vegetales)
vegetales[1]="Ajo"
print(vegetales)
last_vege=len(vegetales)-1
vegetales[last_vege]="Aji"
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora pasemos a la comprobación de elementos en una lista
#Comprobar un elemento si es miembro de una lista usando en operador. Vea el ejemplo a continuación.
frutas = ['platano', 'naranja', 'mango', 'manzana']
existe='platano' in frutas#in lo usamos para comprobar
print(existe)
no_existe='durazno' in frutas
print(no_existe)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora pasemos a inserta elementos a una lista ya existente 
#Para agregar un elemento al final de una lista existente, utilizamos el método append().
lacteaos= ['leche', 'mantequilla', 'queso', 'yoghurt']
lacteaos.append('helado')#Se llama la lista junto a append y dentro de los paréntesis el elemento nuevo
print(lacteaos)
nuevo='Queso de corte'
lacteaos.append(nuevo)#podemos usar variables 
print(lacteaos)
n1=False
lacteaos.append(n1)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora insertemos elementos
#Podemos usar insert() método para insertar un único elemento en un índice especificado en una lista. Tenga en cuenta que otros elementos se desplazan hacia la derecha.
#El insert() methods toma dos argumentos:index y un elemento para insertar.
paises = ['Argentina', 'Colombia', 'Chile', 'Bolivia', 'Perú']
paises.insert(2,'Panamá ')#Panamá se podrán entre Colombia y Chile 
print(paises)
dos='Uruguay','Brasil'
paises.insert(4,dos)
print(paises)
#Ahora borremos elementos de una lista
#El método de eliminación elimina un elemento especificado de una lista remove()
alumnos=['Julian','Diego','Alejandro','Marcos','Pablo']
alumnos.remove('Diego')
print(alumnos)
borrar='Alejandro'
alumnos.remove(borrar)
print(alumnos)
#-------------------------------------------------------------------------------------------------------------------------------------------
#El clear() método vacía la lista:
lista=['item1','item2','item3','item4','item5','item6']
lista.clear()
print(lista)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Es posible copiar una lista reasignándola a una nueva variable de la siguiente manera: list2 = list1.
#Ahora, list2 es una referencia de list1, cualquier cambio que hagamos en list2 también modificará el original, list1.
#Pero hay muchos casos en los que no nos gusta modificar el original, sino que nos gusta tener una copia diferente.
#Una de las formas de evitar el problema anterior es usar copy().
vegetales = ['Tomate', 'Papa', 'Palta','Cebolla', 'Zanahoria']
copia_vegetales=vegetales.copy()
print(copia_vegetales)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora unamos listas
#Hay varias formas de unir o concatenar dos o más listas en Python.
#Plus Operador (+)
lista=['item1','item2','item3','item4','item5','item6']
lista2=['item7','item8','item9','item10','item11','item12']
lista3=lista+lista2
print(lista3)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Unirse usando el método extend() El extend() el método permite añadir una lista en una lista. Vea el ejemplo a continuación.
numeros=[1,3,5,6,8]
numeros2=[2,4,7,9]
numeros.extend(numeros2)
print(numeros)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Contar Artículos en una Lista
#El count() método devuelve el número de veces que aparece un elemento en una lista:
frutas = ['platano', 'naranja', 'mango', 'manzana']
print(frutas.count('mango'))
print(frutas.count('naranja'))
#-------------------------------------------------------------------------------------------------------------------------------------------
#El index() método devuelve el índice de un elemento en la lista:
lacteaos= ['leche', 'mantequilla', 'queso', 'yoghurt']
print(lacteaos.index('queso'))
print(lacteaos.index('mantequilla'))
#-------------------------------------------------------------------------------------------------------------------------------------------
#Revertir una Lista
#El reverse() el método invierte el orden de una lista.
años=[2005,2003,2001,2009,2004,2014,2006]
años.reverse()
print(años)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Lista de Clasificación de Artículos
#Para ordenar listas que podemos usar sort() método o sorted() funciones integradas. 
#El sort() el método reordena los elementos de la lista en orden ascendente y modifica la lista original. Si un argumento de sort() el método inverso es igual a verdadero, organizará la lista en orden descendente.
años=[2005,2003,2001,2009,2004,2014,2006]
años.sort()
print(años)
años.sort(reverse=True)
print(años)
#sorted(): devuelve la lista ordenada sin modificar la lista original Ejemplo:
frutas = ['platano', 'naranja', 'mango', 'manzana']
print(sorted(años))
print(sorted(años,reverse=True))
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora ya estas list@ para el Modulo "https://github.com/JulianB0315/Python_0_to_hero/blob/main/Ejercicios/05%20%20Listas/05%20Listas%20.md"