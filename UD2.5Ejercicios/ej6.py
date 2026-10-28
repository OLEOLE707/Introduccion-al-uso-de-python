from datos import series 

lista = [f"La serie {s['titulo']} tiene {len([r for r in s['reseñas']])} reseñas" for s in series ]
print(lista)
