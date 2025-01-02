"""Operaciones básicas con un conjunto"""

# Crear el conjunto frutas
frutas = {'manzana', 'plátano', 'cereza', 'pera'}
# 2. Longitud del conjunto
print(len(frutas))  
# 3. Añadir 'mango'
frutas.add('mango')
print(frutas)  
# 4. Añadir múltiples frutas
frutas.update({'uva', 'kiwi', 'fresa'})
print(frutas) 
# 5. Eliminar 'pera' con remove
frutas.remove('pera')
print(frutas)  
# Eliminar 'cereza' con discard
frutas.discard('cereza')
print(frutas)  

"""Comprobación de subconjunto y superconjunto"""

# Crear el conjunto A
A = {1, 2, 3, 4, 5}
# 2. Comprobar si A es un subconjunto de {1, 2, 3, 4, 5, 6, 7}
conjunto_b = {1, 2, 3, 4, 5, 6, 7}
print(A.issubset(conjunto_b))  
# 3. Comprobar si A es un superconjunto de {1, 2, 3}
conjunto_c = {1, 2, 3}
print(A.issuperset(conjunto_c))

"""Diferencia y diferencia simétrica"""

# Crear el conjunto numeros
numeros = {1, 2, 3, 4, 5, 6}
# 2. Diferencia entre numeros y {4, 5, 6, 7, 8}
conjunto_d = {4, 5, 6, 7, 8}
print(numeros - conjunto_d)  
# 3. Diferencia simétrica entre numeros y {4, 5, 6, 7, 8}
print(numeros ^ conjunto_d) 

"""Conversiones y tamaño"""

# Crear la lista edades
edades = [12, 15, 18, 20, 12, 15, 18]
# 2. Convertir la lista en un conjunto
edades_set = set(edades)
# 3. Comparar longitudes
print(len(edades))  
print(len(edades_set))  


"""Palabras únicas en una frase"""
# Crear la frase
frase = "Me gusta aprender Python y disfrutar de la programación"

# 2. Convertir la frase en un conjunto de palabras únicas
palabras = set(frase.split())

# 3. Mostrar la cantidad de palabras únicas
print(len(palabras)) 
