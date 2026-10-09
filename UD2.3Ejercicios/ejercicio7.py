from datos import pokemons

for pokemon in pokemons[:]:
    if "Normal" in pokemon["tipos"]:
        pokemons.remove(pokemon)

for pokemon in pokemons:
    print(pokemon["nombre"], pokemon["tipos"])
