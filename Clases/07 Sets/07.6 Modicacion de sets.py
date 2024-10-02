#-------------------------------------------------------------------------------------------------------------------------------------------
#Para eliminar un elemento de un conjunto en Python, puedes usar los métodos remove(), discard(), o pop().
#-------------------------------------------------------------------------------------------------------------------------------------------
#remove(elemento): Elimina el elemento especificado. Si el elemento no está presente, se lanza un KeyError.
mi_set = {1, 2, 3, 4}
mi_set.remove(3)
print(mi_set)  # Salida: {1, 2, 4}
# mi_set.remove(5)  # Esto causará un KeyError
#discard(elemento): Elimina el elemento especificado sin lanzar un error si el elemento no está presente.
mi_set = {1, 2, 3, 4}
mi_set.discard(2)
print(mi_set)  # Salida: {1, 3, 4}
mi_set.discard(5)  # No ocurre error, simplemente no se elimina nada
