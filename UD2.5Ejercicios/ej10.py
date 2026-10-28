from datos import series 

lista = [r["usuario"] for s in series for r in s["reseñas"] if "Drama" in s["generos"]]
print(lista)
