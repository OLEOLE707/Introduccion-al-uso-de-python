from datos import jugadores

lista = [j for j in jugadores if "ruleta" in j["filigranas"]]
print(lista)