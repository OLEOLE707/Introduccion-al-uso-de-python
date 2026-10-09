from datos import personajes_frieren

for personaje in personajes_frieren:
    if personaje["raza"] == "Humano" and personaje["edad"] >= 100:
        personaje["raza"] = "Zombie"

    print(personaje["nombre"], personaje["raza"])