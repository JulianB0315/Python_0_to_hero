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