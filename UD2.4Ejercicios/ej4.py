from datos import jugadores

lista = [j["nombre"] for j in jugadores if j["atributos"]["pase"] >= 9]
print(lista)