import csv

def get_game_data():
    """
    Collects video game information from user input.
    Returns a list of dictionaries containing game details.
    """
    games_list = []
    while True:
        print("\nIngrese los datos de los juegos (o escriba 'fin' para terminar):")
        nombre = input("Nombre del juego: ")
        # Check if user wants to stop entering data
        if nombre.lower() == 'fin':
            break
            
        # Create dictionary with game information
        game = {
            'nombre': nombre,
            'genre': input("Genero: "),
            'developer': input("Developer: "),
            'classification': input("ESRB Rating: ")
        }
        games_list.append(game)  # Add game to the list
    return games_list

# Define headers for CSV file
game_headers = (
    'nombre',
    'genre',
    'developer',
    'classification',
)

def write_csv_file(file_path, data, headers):
    """
    Writes game data to a CSV file.
    Parameters:
        file_path (str): Path to the output CSV file
        data (list): List of dictionaries containing game data
        headers (tuple): Column headers for the CSV file
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()  # Write the column headers
        writer.writerows(data)  # Write all game data

def main():
    """
    Main function that orchestrates the program flow:
    1. Collects game data from user
    2. Writes data to CSV file
    3. Displays confirmation message
    """
    games_data = get_game_data()
    write_csv_file('games.csv', games_data, game_headers)
    print("\nLos datos han sido guardados en 'games.csv'")

# Execute main function only if script is run directly
if __name__ == "__main__":
    main()