from datos import pokemons

mayor_peso = pokemons[0]

for pokemon in pokemons:
    if( pokemon["peso_kg"] > mayor_peso["peso_kg"]):
        
        mayor_peso = pokemon

print(mayor_peso["nombre"], " = ", mayor_peso["peso_kg"])
