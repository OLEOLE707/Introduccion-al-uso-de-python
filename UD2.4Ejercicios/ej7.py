from datos import jugadores


lista = [f"{j['nombre']} - Pase: {j['atributos']['pase']}" for j in jugadores]