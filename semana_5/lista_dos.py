def oracion_reversa(my_string):
    counter = 0
    for i in range(len(oracion) - 1, -1, -1):
        print(oracion[i], end=' ')
        counter += 1
        if counter % 3 == 0:  # Cada 3 caracteres
            print()  # Imprime un salto de línea

# Ejemplo de uso
oracion = 'Hola mundo mundial'
oracion_reversa(oracion)