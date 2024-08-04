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