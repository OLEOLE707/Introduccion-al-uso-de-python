from datos import pokemons

suma=0
contador=0

for pokemon in pokemons:
    suma+=pokemon["altura_m"]
    contador +=1

media=suma/contador

for pokemon in pokemons:
    if (pokemon["altura_m"]> media):
        print(pokemon["nombre"], " : ", pokemon["altura_m"])

