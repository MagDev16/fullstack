# ==============================================================================
# BUBBLE SORT (De derecha a izquierda - Burbujas menores a la izquierda)
# ==============================================================================

def bubble_sort_right_to_left(list):
    n = len(list)
    
    # Typically traverse the list during each pass
    for i in range(n):
        swapped = False

        # The inner loop now iterates FROM RIGHT TO LEFT
        for j in range(n - 1, i, -1):
            
            # If the element on the right is SMALLER than the one 
            # on the left, we swap them
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                swapped = True

        # Optimization: if no swaps occurred, the list is already sorted
        if not swapped:
            break
        
    return list

# ==============================================================================
# CASO DE PRUEBA Y DEMOSTRACIÓN
# ==============================================================================

if __name__ =="__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    print("La lista original:", numbers)
    bubble_sort_right_to_left(numbers)
    print("Lista ordenada (menores a la izquierda):", numbers)