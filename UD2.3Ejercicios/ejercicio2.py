from datos import pokemons

suma=0
contador=0

for pokemon in pokemons:
    suma+=pokemon["altura_m"]
    contador +=1

resultado=suma/contador

print(resultado)