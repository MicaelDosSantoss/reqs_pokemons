import requests
import json

req_number_poke = requests.get("https://pokeapi.co/api/v2/pokedex/1/")
req_number_poke_JSON = req_number_poke.json()

number_total_poke = len(req_number_poke_JSON["pokemon_entries"]) + 1

list_pokemons = []

for i in range(1,number_total_poke):
    link_publ = f"https://pokeapi.co/api/v2/pokemon/{i}/"

    api_req = requests.get(link_publ)
    api_req_JSON = api_req.json()

    num = len(api_req_JSON["types"]) 

    list_type_pokemon = []

    for j in range(0,num):
        list_type_pokemon.append(api_req_JSON["types"][j]["type"]["name"])

    list_pokemons.append({'numero': i,'pokemon': api_req_JSON["species"]["name"],'tipos':list_type_pokemon})

with open('Pokedex.json', 'w') as pokedex_json: 
    json.dump(list_pokemons, pokedex_json, indent=2)

