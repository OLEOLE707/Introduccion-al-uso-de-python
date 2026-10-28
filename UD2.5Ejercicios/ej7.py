from datos import series 

lista = [f"({s['titulo']}, {([r for r in s['reseñas'] if r['nota'] == 10])})" for s in series if 10 in [r['nota'] for r in s['reseñas']] ]
print(lista)
