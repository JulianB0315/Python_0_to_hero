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