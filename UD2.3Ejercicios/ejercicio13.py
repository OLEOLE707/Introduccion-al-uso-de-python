from datos import personajes_frieren


for personaje in personajes_frieren:
    if "Elfo" in personaje["raza"]:
        personaje["afiliacion"].append("Elfos Supervivientes del Examen de Python")

    print(personaje["nombre"],personaje["raza"], personaje["afiliacion"])


