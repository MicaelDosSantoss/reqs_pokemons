import requests
import json


generation_poke = requests.get(f"https://pokeapi.co/api/v2/generation/1/")
generation_poke_JSON = generation_poke.json()

number_generation = len(generation_poke_JSON["pokemon_species"])
for num in range(number_generation):
    generation_poke = generation_poke_JSON["main_region"]["name"]
    pokemon_name = generation_poke_JSON["pokemon_species"][num]["name"]
    print(generation_poke,pokemon_name)

