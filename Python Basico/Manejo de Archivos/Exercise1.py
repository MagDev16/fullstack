def save_songs(input_file):
    """
    Create a file with songs names then save it on new file.
    Parameters:
    input_file (str): File name use to storage songs names.
    """
    try:
        # Ask user for songs names
        print(f"Ingrese los nombres de las canciones que desea guardar en el archivo (escriba 'fin' para terminar de agregar canciones): ")
        songs = []
        while True:
            song = input("Ingrese el nombre de la canción: ")
            if song.lower() == 'fin':  # End loop if user types 'fin'
                break
            songs.append(song)  # Add song to the 'songs' list
            
        # Save songs on file  
        with open(input_file, 'w') as file:
            for song in songs:
                file.write(song + '\n')
                
        print(f"Los nombres de las canciones se han guardado en '{input_file}'.")
    except Exception as e:
        print(f"Ocurrió un error al guardar las canciones: {e}")
        
        
def read_and_order_songs(input_file, output_file):
    """
    Read songs names from file and order them alphabetically.
    Parameters:
    input_file (str): File name use to storage songs names.
    output_file (str): File name use to storage ordered songs names.
    """
    try:
        # Read songs from file
        with open(input_file, 'r') as file:
            songs = file.readlines()  # Read all lines from file
            songs = [song.strip() for song in songs]  # Remove newline characters
            songs.sort()  # Order songs alphabetically
            
        with open(output_file, 'w') as file:
            for song in songs:
                file.write(song + '\n')  # Write songs on file
                
        print(f"Los nombres de las canciones se han ordenado alfabéticamente y se han guardado en '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: El archivo '{input_file}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def main():
    # Ask user for input and output file names
    input_file = input("Ingrese el nombre del archivo para guardar las canciones (por ejemplo, 'canciones.txt'): ")
    output_file = input("Ingrese el nombre del archivo de salida (por ejemplo, 'canciones_ordenadas.txt'): ")

    save_songs(input_file)  # Call function to save songs
    read_and_order_songs(input_file, output_file)  # Call function to read and order songs

if __name__ == "__main__":
    main()