from datos import personajes_frieren

suma=0
contador=0

for personaje in personajes_frieren:
    if "Humano" in personaje["raza"]:
        suma+=personaje["edad"]
        contador +=1

media=suma/contador

print("Media: ",media)

