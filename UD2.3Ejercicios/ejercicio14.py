from datos import personajes_frieren

for personaje in personajes_frieren:
    if "Asociación Continental de Magia" in personaje["afiliacion"]:
        personaje["afiliacion"].remove("Asociación Continental de Magia")

    print(personaje["nombre"], personaje["afiliacion"])