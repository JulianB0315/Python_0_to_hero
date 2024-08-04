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