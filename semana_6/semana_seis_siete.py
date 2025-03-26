print('------------------------------------------------------------')
print('Función que acepte una lista de números y retorne una lista-')
print('------------------------------------------------------------')

# Auxiliary function to verify if a number is prime
def prime_number(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not primes
    if num == 2:
        return True  # 2 is the only prime even number
    if num % 2 == 0:
        return False  # Discard even numbers greater than 2

    # Verify divisibility from 3 to the square root of the number
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False  # If it is divisible, it is not prime
    return True  # If it is not divisible by any number, it is prime


# Main function to filter prime numbers from a list
def filter_primes(list_numbers):
    prime_numbers = []  # List ready to store prime numbers
    for num in list_numbers:
        if prime_number(num):  # Check if the number is prime
            prime_numbers.append(num)  # Add to prime list
    return prime_numbers

# Request the user to enter a list of numbers
user_entry = input("Ingresa una lista de números separados por comas: ")

# Convert user input to integer list
try:
    list_numbers = [int(num) for num in user_entry.split(",")]
except ValueError:
    print("Error: Asegúrate de ingresar solo números separados por comas.")
    exit()

# Call the function and show the result
prime_numbers = filter_primes(list_numbers)
print("Números primos en la lista:", prime_numbers)