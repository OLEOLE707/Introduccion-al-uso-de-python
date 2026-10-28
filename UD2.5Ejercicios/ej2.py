from datos import series 

lista = [s["titulo"] for s in series if ("Fantasía" in s["generos"] or "Misterio" in s["generos"])]
print(lista)