# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🎮
# ****🤖Programador:Julia Burga Bracamonte******
# **********************************************
# ****🔒GitHub:https://github.com/JulianB0315 **    
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🏀
#-------------------------------------------------------------------------------------------------------------------------------------------
#Anteriormente vimos las listas, pero solo como un tipo de dato, pero ¿Qué son las listas y cuáles son?
#Hay cuatro tipos de datos de recopilación en Python
#Estos son list,Tuple,Set,Dictionary
#List: es una colección que está ordenada y cambiante(modificable). Permite miembros duplicados.
#Tuple: es una colección ordenada e inmutable o no modificable(inmutable). Permite miembros duplicados.
#Set: es una colección que no está ordenada, no está indexada y no es modificable, pero podemos agregar nuevos elementos al conjunto. No se permiten miembros duplicados.
#Dictionary:es una colección que es desordenada, cambiante(modificable) e indexada. Sin miembros duplicados.
#Una lista es la recopilación de diferentes tipos de datos que están ordenados y modificables(mutables). Una lista puede estar vacía o puede tener diferentes elementos de tipo de datos.
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora que sabemos todo esto hagamos una lista
#Hay dos maneras de hacer lista como paréntesis o con corchetes
empty_list = list() #Dentro de los paréntesis debes de poner los elementos de tu lista 
print(len(empty_list))#0 por no haber elementos
empty_list = [] #Dentro de los corchetes debes de poner los elementos 
print(len(empty_list)) # 0 por no haber elementos
#Usemos las función len() para contar los elementos de la lista 
#Creamos las listas 
frutas = ['platano', 'naranja', 'mango', 'manzana']
vegetales = ['Tomate', 'Papa', 'Palta','Cebolla', 'Zanahoria']
lacteaos= ['leche', 'mantequilla', 'queso', 'yoghurt']
web= ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']
paises = ['Argentina', 'Colombia', 'Chile', 'Bolivia', 'Perú']
#mostramos
print('Frutas:', frutas)
print('Cantidad de frutas:', len(frutas))
print('Vegetales:', vegetales)
print('Cantidad de vegetales:', len(vegetales))
print('Lacteos',lacteaos)
print('Cantidad de lacteos:', len(lacteaos))
print('Web:', web)
print('NCantidad de web:', len(web))
print('Paises:', paises)
print('Cantidad de paises:', len(paises))
#-------------------------------------------------------------------------------------------------------------------------------------------
#Una lista puede contener diferentes tipos de elementos
lista = ['Juan', 250, True, {'Pais':'Perú', 'Cuidad':'Lima'}]