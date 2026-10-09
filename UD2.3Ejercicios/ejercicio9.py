from datos import personajes_frieren

for personaje in personajes_frieren[:]:
    if "Magos de Primera Clase" in personaje["afiliacion"]:
        print(personaje["nombre"],", ", personaje["raza"], " : ", personaje["afiliacion"])
