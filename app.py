import requests
import json

req_number_poke = requests.get("https://pokeapi.co/api/v2/pokedex/1/")
req_number_poke_JSON = req_number_poke.json()

number_total_poke = len(req_number_poke_JSON["pokemon_entries"]) + 1

list_pokemons = []

for i in range(1, number_total_poke):
    link_publ = f"https://pokeapi.co/api/v2/pokemon/{i}/"

    api_req = requests.get(link_publ)
    api_req_JSON = api_req.json()

    list_type_pokemon = [type_data["type"]["name"] for type_data in api_req_JSON["types"]]

    generation = ""
    for u in range(1, 10):  # Supondo que você queira verificar as gerações de 1 a 7
        generation_poke = requests.get(f"https://pokeapi.co/api/v2/generation/{u}/")
        generation_poke_JSON = generation_poke.json()

        pokemon_names_in_generation = [pokemon["name"] for pokemon in generation_poke_JSON["pokemon_species"]]
        if api_req_JSON["species"]["name"] in pokemon_names_in_generation:
            generation = generation_poke_JSON["main_region"]["name"]
            break  # Interrompe a busca se o Pokémon for encontrado em uma geração

    list_pokemons.append({'geracao': generation, 'numero': i, 'pokemon': api_req_JSON["species"]["name"], 'tipos': list_type_pokemon})

with open('Pokedex.json', 'w') as pokedex_json:
    json.dump(list_pokemons, pokedex_json, indent=2)