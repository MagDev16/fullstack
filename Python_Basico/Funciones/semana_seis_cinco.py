print('------------------------------------------------------------')
print('-imprimir el numero de mayúsculas y el numero de minúsculas-')
print('------------------------------------------------------------')


def count_uppercase_lowercase(text_string):
    capital_letters = 0  # capital letter counter
    lowercase_letters = 0  # lowercase counter

    # Run each character in the string
    for character in text_string:
        if character.isupper():  # Check if the character is capital
            capital_letters += 1
        elif character.islower():  # Check if the character is lowercase
            lowercase_letters += 1

    # Imprimir el resultado
    print(f"Hay {capital_letters} mayúsculas y {lowercase_letters} minúsculas")

# Request the user to enter a text string
text_string = input("Ingresa una cadena de texto: ")

# Call function for upper and lower case counting
count_uppercase_lowercase(text_string)