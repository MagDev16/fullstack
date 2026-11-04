# ==============================================================================
# Análisis de Algoritmos
# ==============================================================================

def print_numbers_times_2(numbers_list):    # O(1)
	for number in numbers_list: # O(n) 'n' es la cantidad de elementos en la lista
		print(number * 2)   # O(1) por cada multiplicacion e impresion

# ==============================================================================

def check_if_lists_have_an_equal(list_a, list_b):   # O(1)
	for element_a in list_a:    # O(n) 'n' es la longitud de la list_a
		for element_b in list_b:    # O(M) por cada elemento de list_a (M es la longitud de list_b)
			if element_a == element_b:   # O(1)
				return True # O(1)
				
	return False    # O(1)

# ==============================================================================

def print_10_or_less_elements(list_to_print):   # O(1)
	list_len = len(list_to_print)   # O(1)
	for index in range(min(list_len, 10)):  # O(1) porque el bucle se ejecuta como maximo 10 veces (es un limite constante)
		print(list_to_print[index])     # O(1)

# ==============================================================================

def generate_list_trios(list_a, list_b, list_c):    # O(1)
	result_list = []    # O(1)
	for element_a in list_a:    # O(n) 'n' es la longitud de list_a
		for element_b in list_b:    # O(M) por cada elemento de list_a (M es la longitud de list_b)
			for element_c in list_c:    # O(K) por cada combinación de A y B (K es la longitud de list_c)
				result_list.append(f'{element_a} {element_b} {element_c}')  # O(1)
				
	return result_list  # O(1)