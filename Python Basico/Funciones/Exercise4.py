print('--------------------------------------------------------')
print('--Función que le de la vuelta a un string y lo retorne--')
print('--------------------------------------------------------')

def reverse_string(text):
    """
    Parameters:
    text (str): The string to invert.

    Return:
    str: The inverted string.
    """
    inverted = ""
    for character in text:
        inverted = character + inverted
    return inverted

# Request the user to enter the original text
original_text = input("Ingresa el texto que deseas invertir: ")

# Call function to invert text
reverse_text = reverse_string(original_text)

# Show result
print(f'Original: "{original_text}" -> Invertido: "{reverse_text}"')
