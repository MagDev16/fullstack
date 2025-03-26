my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = []  # Lista vacía para guardar los pares

for num in my_list:        # Recorremos cada elemento de la lista original
    if num % 2 == 0:       # Verificamos si el número es par
        even_list.append(num)  # Si es par, lo agregamos a even_list

print(even_list) 