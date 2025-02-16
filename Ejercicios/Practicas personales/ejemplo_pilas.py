class Pila:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)

# Uso de la pila
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)

print(pila.peek())  # Ver el elemento superior
print(pila.pop())   # Eliminar el elemento superior
print(pila.size())  # Ver el tamaño de la pila