from datos import jugadores

lista = [j["nombre"] for j in jugadores if j["equipo"] == "FC Barcelona"]
print(lista)