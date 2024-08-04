"""Acceso a elementos:"""
program = ["Python", "Java", "C++", "JavaScript"]
#Usando indexación positiva
print(program[0])  
print(program[1])  
print(program[2])  
print(program[3])  
#Usando indexación negativa
print(program[-1])  
print(program[-2])  
print(program[-3])  
print(program[-4])  
"""Modificación de elementos:"""

pc = ["CPU", "RAM", "GPU", "HDD"]
print(pc)
# Cambiar elementos usando indexación positiva
pc[1] = "SSD"
print(pc)  
# Cambiar elementos usando indexación negativa
pc[-1] = "PSU"
print(pc)  
# Comprobar si un elemento está en la lista
print("GPU" in pc)
# Usar append() para añadir un elemento al final de la lista
print("RAM" in pc)
pc.append("Motherboard")
print(pc)  
# Usar insert() para añadir un elemento en una posición específica
pc.insert(2, "RAM")
print(pc) 
# Crear la lista procesadores
procesadores = ["Intel", "AMD"]
# Unir la lista procesadores a la lista pc con extend()
pc.extend(procesadores)
print(pc)
# Ordenar la lista con sort() (modifica la lista original)
pc.sort()
print(pc)

# Ordenar la lista con sorted() (crea una nueva lista ordenada)
pc_sorted = sorted(pc)  
print(sorted(pc,reverse=True))

# Eliminar un elemento específico
pc.remove("Intel")
print(pc) 
# Limpiar la lista con clear()
pc.clear()
print(pc) 