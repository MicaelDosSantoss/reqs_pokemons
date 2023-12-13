import requests
import json

generation_list_poke = []

# generation = ""
for u in range(1, 10):  # Supondo que você queira verificar as gerações de 1 a 9
    generation_poke = requests.get(f"https://pokeapi.co/api/v2/generation/{u}/")
    generation_poke_JSON = generation_poke.json()
    
    pokemon_names_in_generation = []
    pokemon_names_in_generation.append([pokemon["name"] for pokemon in generation_poke_JSON["pokemon_species"]])

    generation_list_poke.append({'geracao': generation_poke_JSON["main_region"]["name"], 'pokemons': pokemon_names_in_generation})

with open('generation.json','w') as  generation_json:
    json.dump(generation_list_poke,generation_json,indent=2)       
    