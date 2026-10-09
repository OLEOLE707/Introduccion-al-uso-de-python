from datos import personajes_frieren

personajes_frieren.append(
    {
    "nombre": "Kanne",
    "raza": "Humano",
    "clase": "Mago",
    "edad": 19,
    "afiliacion": ["Magos de Primera Clase", "Grupo de Frieren"]
    }
)

for personajes in personajes_frieren:
    print(personajes["nombre"])