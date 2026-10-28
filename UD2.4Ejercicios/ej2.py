from datos import jugadores 

for jugador in jugadores:
    if jugador["dorsal"] == 10:
        print(f"{jugador['nombre']} - Dorsal: {jugador['dorsal']}")

lista = [j for j in jugadores  if j["dorsal"] == 10]
print(lista)