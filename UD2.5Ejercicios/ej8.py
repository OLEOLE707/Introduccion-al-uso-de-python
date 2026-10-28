from datos import series

lista= [(s["titulo"], "Obra maestra" if sum(r["nota"] for r in s["reseñas"]) / len(s["reseñas"]) >= 9 else "Gran serie") for s in series]
print(lista)