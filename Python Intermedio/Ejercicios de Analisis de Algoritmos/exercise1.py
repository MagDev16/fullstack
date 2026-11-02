# ==============================================================================
# Análisis de Algoritmos
# ==============================================================================

def bubble_sort_right_to_left(list):    # O(1)
    n = len(list)   # O(1)
    
    for i in range(n):  # O(n)
        swapped = False # O(1)

        for j in range(n - 1, i, -1):   # O(n^2)
            
            if list[j] < list[j - 1]:   # O(1)
                list[j], list[j - 1] = list[j - 1], list[j] # O(1)
                swapped = True  # O(1)

        if not swapped: # O(1)
            break   # O(1)
        
    return list # O(1)


if __name__ =="__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]  # O(1)
    
    print("La lista original:", numbers)    # O(1)
    bubble_sort_right_to_left(numbers)  # O(n^2) it executes the entire function
    print("Lista ordenada (menores a la izquierda):", numbers)  # O(1)