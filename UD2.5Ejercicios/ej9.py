from datos import series

lista = [g for s in series for g in s["generos"]]
print(lista)