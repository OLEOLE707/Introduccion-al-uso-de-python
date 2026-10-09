from datos import personajes_frieren

for personaje in personajes_frieren[:]:
    if "Grupo de los Cuatro Héroes" in personaje["afiliacion"]:
        print(personaje["nombre"],",", personaje["raza"], " : ", personaje["edad"])
