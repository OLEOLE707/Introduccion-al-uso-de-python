from datos import series 

lista = [s["titulo"] for s in series if  s["nota"] >= 9 and len(s["generos"]) > 3]
print(lista)