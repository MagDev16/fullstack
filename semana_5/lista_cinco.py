# Solicitar 10 números al usuario
numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

# Mostrar la lista y el número más alto
print("Números ingresados:", numeros)
print(f"El más alto fue {max(numeros)}")