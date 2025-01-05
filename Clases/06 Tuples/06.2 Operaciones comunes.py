#-------------------------------------------------------------------------------------------------------------------------------------------
#Indexación Positiva
# Similar al tipo de datos de lista, utilizamos la indexación positiva o negativa para acceder a los elementos de tupla.
frutas = ('platano', 'naranja', 'mango', 'manzana')
#            0           1         2         3
arti_1=frutas[0]
print(arti_1)
arti_2=frutas[1]
print(arti_2)
arti_3=len(frutas)-1
print(arti_3)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Indexación negativa 
#Medios de indexación negativos que comienzan desde el final, 
#-1 se refiere al último elemento, -2 se refiere al segundo último y el negativo de la longitud de lista/tupla se refiere al primer elemento.
vegetales = ('Tomate', 'Papa', 'Palta','Cebolla', 'Zanahoria')
#              -5       -4        -3      -2           -1
arti1 = vegetales[-4]
print(arti1)
arti2 = vegetales[-3]
print(arti2)
ulti_vege= vegetales[-1]
print(ulti_vege)
#Ahora aprendamos a cortar los artículos de los tuples 
#Podemos cortar una subtupla especificando un rango de índices por dónde empezar y por dónde terminar en la tupla, 
#el valor de retorno será una nueva tupla con los elementos especificados.
#Rango de index positivo
tpl=('item1','item2','item3','item4','item5')
todo=tpl[0:5]
print(todo)
todos=tpl[0:]
print(todos)
dos_items=tpl[1:3]
print(dos_items)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Rango de index negativo
frutas=('manzana','pera','durazno','sandia')
todas = frutas[-4:]
print(todas)
pera_sandia = frutas[-3:-1]
print(pera_sandia)
todas2 = frutas[-3:]
print(todas2)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora cambiemos de tuples a listas 
#Podemos cambiar tuplas a listas y listas a tuplas. Tuple es inmutable si queremos modificar una tupla debemos cambiarla a una lista.
tpl = ('item1', 'item2', 'item3','item4','item5','item6','item7')
lst = list(tpl)
print(lst)
tpl2=tuple(lst)
print(tpl2)
#-------------------------------------------------------------------------------------------------------------------------------------------
#ahora comprobemos los artículos de una tuples
tpl = ('item1', 'item2', 'item3','item4','item5','item6','item7')
print('item10' in tpl)
print('item4' in tpl)
print('item100' in tpl)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Union de tuples
#Podemos unir dos o más tuplas usando + operador
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
print(tpl3)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Eliminar Tuples
#No es posible eliminar un solo elemento en una tupla, pero es posible eliminar la tupla usando del.
tpl1 = ('item1', 'item2', 'item3')
del tpl1
#print(tpl1) no existe
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora ya estas list@ para el Modulo "https://github.com/JulianB0315/Python_0_to_hero/blob/main/Ejercicios/06%20Tuples/05%20Listas%20.md"
