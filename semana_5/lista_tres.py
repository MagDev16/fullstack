def nueva_lista(lista):
    # Verificamos que la lista tenga al menos 2 elementos
    if len(lista) < 2:
        return lista
    
    # Guardamos el primer elemento en una variable temporal
    temporal = lista[0]
    # El primer elemento ahora es el último
    lista[0] = lista[-1]
    # El último elemento ahora es el que guardamos en temp
    lista[-1] = temporal
    
    return lista

# Ejemplo de uso
lista = [66, 3, 62346, 1, 24]
result = nueva_lista(lista)
print(result)  # [7, 3, 6, 1, 4]