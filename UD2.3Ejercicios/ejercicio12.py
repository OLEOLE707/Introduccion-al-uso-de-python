from datos import personajes_frieren

for personaje in personajes_frieren[:]:
    if "Demonio" in personaje["raza"]:
        personajes_frieren.remove(personaje)

for personajes in personajes_frieren:
    print(personajes["nombre"], personajes["raza"])
