import json

<<<<<<< HEAD
def load_pokemons(archivo):
    """Loads existing pokémon from a JSON file"""
    try:
        with open(archivo, 'r') as f: # Open file in read mode
=======
def load_pokemons(file):
    """Loads existing pokemon from a JSON file"""
    try:
        with open(file, 'r') as f: # Open file in read mode
>>>>>>> eb9846e0efa2fa5bd94a54df49d89098f31d3f77
            return json.load(f) # Load JSON data from file
    except FileNotFoundError:
        return []

def enter_new_pokemon():
<<<<<<< HEAD
    """Requests user data for a new Pokémon"""
    print("\nIngrese los datos del nuevo Pokémon:")
    
    nombre = input("Nombre en inglés: ").strip() # Request English name and clear spaces with .strip()
=======
    """Requests user data for a new Pokemon"""
    print("\nIngrese los datos del nuevo Pokémon:")
    
    name = input("Nombre en inglés: ").strip() # Request English name and clear spaces with .strip()
>>>>>>> eb9846e0efa2fa5bd94a54df49d89098f31d3f77
    
    print("Tipos (separados por coma si tiene más de uno):")
    types = [t.strip() for t in input("Ej: Fire, Water, Electric: ").split(',')] # Request types and clear spaces with.strip()
    
    print("\nEstadísticas base del Pokémon: ")
    base = { # Request base stats
        'HP': int(input("HP: ")),
        'Attack': int(input("Attack: ")),
        'Defense': int(input("Defense: ")),
        'Sp. Attack': int(input("Sp. Attack: ")),
        'Sp. Defense': int(input("Sp. Defense: ")),
        'Speed': int(input("Speed: "))
    }
    
    return { # Return dictionary with Pokémon data
<<<<<<< HEAD
        'name': {'english': nombre},
=======
        'name': {'english': name},
>>>>>>> eb9846e0efa2fa5bd94a54df49d89098f31d3f77
        'type': types,
        'base': base
    }

<<<<<<< HEAD
def save_pokemons(archivo, datos):
    """Saves the list of pokémon in a JSON file"""
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent=2)
    print(f"\nDatos del Pokémon guardados correctamente en {archivo}")
=======
def save_pokemons(file, data):
    """Saves the list of pokémon in a JSON file"""
    with open(file, 'w') as f:
        json.dump(data, f, indent=2) # Save JSON data to file with indentation for readability
    print(f"\nDatos del Pokémon guardados correctamente en {file}")
>>>>>>> eb9846e0efa2fa5bd94a54df49d89098f31d3f77

def display_pokemons(pokemons):
    """Displays the list of all pokémon and their details"""
    print("\nLista de Pokémon capturados:")
    print("-" * 50)
    for pokemon in pokemons:
        print(f"Nombre: {pokemon['name']['english']}")
        print(f"Tipos: {', '.join(pokemon['type'])}")
        print("Estadísticas base:")
<<<<<<< HEAD
        for stat, value in pokemon['base'].items():
            print(f"  {stat}: {value}")
        print("-" * 50)

def main():
    ARCHIVO_JSON = 'pokedex.json'
    
    # Load existing pokémon
    pokemons = load_pokemons(ARCHIVO_JSON)
=======
        for stat, value in pokemon['base'].items(): # Iterate over base stats
            print(f"  {stat}: {value}") # Print stat and value
        print("-" * 50)

def main():
    FILE_JSON = 'pokedex.json'
    
    # Load existing pokémon
    pokemons = load_pokemons(FILE_JSON) 
>>>>>>> eb9846e0efa2fa5bd94a54df49d89098f31d3f77
    print(f"\nTienes {len(pokemons)} Pokémon(s) en el Pokedex.")
    print("-" * 50)
    
    # Ask for new pokemon
    new_pokemon = enter_new_pokemon()
    pokemons.append(new_pokemon)
    
    # Save pokemons
<<<<<<< HEAD
    save_pokemons(ARCHIVO_JSON, pokemons)
=======
    save_pokemons(FILE_JSON, pokemons)
>>>>>>> eb9846e0efa2fa5bd94a54df49d89098f31d3f77
    
    # Display all pokemons
    display_pokemons(pokemons)

<<<<<<< HEAD
    pokemons = load_pokemons(ARCHIVO_JSON)
=======
    pokemons = load_pokemons(FILE_JSON)
>>>>>>> eb9846e0efa2fa5bd94a54df49d89098f31d3f77
    print(f"\nAhora tienes {len(pokemons)} Pokémon(s) en el Pokedex.")
    print("-" * 50 + f"\n")

if __name__ == "__main__":
    main()