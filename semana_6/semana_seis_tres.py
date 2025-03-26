print('--------------------------------------------------------')
print('---Función que suma todos los elementos de una lista----')
print('--------------------------------------------------------')

def add_list(list_num):
    """
    Parameters:
    lista (list_num): List of numbers to add
    
    Return:
    int o float: The sum of all the items in the list
    """
    num_sum = 0
    for num in list_num:
        num_sum += num
    return num_sum

# Application
numers = [4, 6, 2, 30]
result = add_list(numers)
print(f"La suma de {numers} es: {result}")  # Prints: the result of the sum of the list which is: {result}