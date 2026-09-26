print('------------------------------------------------------------')
print('----Palabras separadas por un guión y retorne un string-----')
print('------------------------------------------------------------')

def sort_words_by_guiones(text_string):
    # Convert the string to a list using the script as a separator
    word_list = text_string.split('-')
    
    # Sort the list alphabetically
    word_list.sort()
    
    # Convert the ordered list back to a scripted string
    chain_ordained = '-'.join(word_list)
    
    return chain_ordained

# Request the user to enter a string
user_string = input("Ingresa un string con palabras separadas por guiones: ")

# Call the function and show the result
result = sort_words_by_guiones(user_string)
print("El string ordenado es:", result)