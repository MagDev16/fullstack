# ==============================================================================
# ALGORITMO BUBBLE SORT
# ==============================================================================

def bubble_sort(list_data):
    n = len(list_data)
    
    # Iteration through all the elements in the list_data
    for i in range(n):
        swapped = False
        
        # The last 'i' elements are already sorted into their correct positions
        for j in range(0, n - i - 1):
            
            # If the current element is greater than the next one, we swap them
            if list_data[j] > list_data[j + 1]:
                list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]
                swapped = True
        
        # Optimization: if no changes occurred during a full pass,
        # it means the list_data is already completely sorted, so we exit.        
        if not swapped:
            break
        
    return list_data

# ==============================================================================
# CASO DE PRUEBA Y DEMOSTRACIÓN
# ==============================================================================

if __name__ == "__main__":
    
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    print("Lista de numeros original:", numbers)
    bubble_sort(numbers)
    print("Lista ordenada:", numbers)