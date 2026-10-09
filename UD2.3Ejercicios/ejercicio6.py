from datos import pokemons

pokemons.append(
        {
    "nombre": "Gengar",
    "generacion": 1,

    "categoria": "Fantasmita",
    "tipos": ["Fantasma", "Veneno"],
    "peso_kg": 40.0,
    "altura_m": 1.5
    }
)

for pokemon in pokemons:
    print(pokemon["nombre"])