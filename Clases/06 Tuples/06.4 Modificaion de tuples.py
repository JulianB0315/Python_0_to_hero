# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🎮
# ****🤖Programador:Julia Burga Bracamonte******
# **********************************************
# ****🔒GitHub:https://github.com/JulianB0315 **    
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🏀
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora cambiemos de tuples a lsitas 
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
#-------------------------------------------------------------------------------------------------------------------------------------------
#Eliminar Tuples
#No es posible eliminar un solo elemento en una tupla, pero es posible eliminar la tupla usando del.
tpl1 = ('item1', 'item2', 'item3')
del tpl1
#-------------------------------------------------------------------------------------------------------------------------------------------
#Ahora ya estas list@ para el Modulo "https://github.com/JulianB0315/Python_0_to_hero/blob/main/Ejercicios/06%20Tuples/05%20Listas%20.md"