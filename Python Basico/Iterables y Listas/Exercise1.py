#Ejercicio 1

def print_lists_together(first_list, second_list):
    # Verificamos que las listas tengan el mismo tamaño
    if len(first_list) != len(second_list):
        print("Las listas deben tener el mismo tamaño")
        return
    
    # Iteramos usando el índice
    result = ""
    for i in range(len(first_list)):
        result += first_list[i] + " " + second_list[i] + " "
    
    print(result)

# Ejemplo de uso
first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

print_lists_together(first_list, second_list)