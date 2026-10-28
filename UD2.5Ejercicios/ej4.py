from datos import series 

lista = [f"{s['titulo']}: {([r for r in s['reseñas'] if r['usuario'] == 'Elena'])} reseñas" for s in series if "Elena" in [r['usuario'] for r in s["reseñas"]] ]
print(lista)
