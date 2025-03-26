import json

def load_pokemons(archivo):
    """Loads existing pokémon from a JSON file"""
    try:
        with open(archivo, 'r') as f: # Open file in read mode
            return json.load(f) # Load JSON data from file
    except FileNotFoundError:
        return []

def enter_new_pokemon():
    """Requests user data for a new Pokémon"""
    print("\nIngrese los datos del nuevo Pokémon:")
    
    nombre = input("Nombre en inglés: ").strip() # Request English name and clear spaces with .strip()
    
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
        'name': {'english': nombre},
        'type': types,
        'base': base
    }

def save_pokemons(archivo, datos):
    """Saves the list of pokémon in a JSON file"""
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent=2)
    print(f"\nDatos del Pokémon guardados correctamente en {archivo}")

def display_pokemons(pokemons):
    """Displays the list of all pokémon and their details"""
    print("\nLista de Pokémon capturados:")
    print("-" * 50)
    for pokemon in pokemons:
        print(f"Nombre: {pokemon['name']['english']}")
        print(f"Tipos: {', '.join(pokemon['type'])}")
        print("Estadísticas base:")
        for stat, value in pokemon['base'].items():
            print(f"  {stat}: {value}")
        print("-" * 50)

def main():
    ARCHIVO_JSON = 'pokedex.json'
    
    # Load existing pokémon
    pokemons = load_pokemons(ARCHIVO_JSON)
    print(f"\nTienes {len(pokemons)} Pokémon(s) en el Pokedex.")
    print("-" * 50)
    
    # Ask for new pokemon
    new_pokemon = enter_new_pokemon()
    pokemons.append(new_pokemon)
    
    # Save pokemons
    save_pokemons(ARCHIVO_JSON, pokemons)
    
    # Display all pokemons
    display_pokemons(pokemons)

    pokemons = load_pokemons(ARCHIVO_JSON)
    print(f"\nAhora tienes {len(pokemons)} Pokémon(s) en el Pokedex.")
    print("-" * 50 + f"\n")

if __name__ == "__main__":
    main()