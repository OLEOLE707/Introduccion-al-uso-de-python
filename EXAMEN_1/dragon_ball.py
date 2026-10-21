from datos import personajes

def ejercicio1():
    print("\n Ejercicio 1")
    personajes.append(
        {"nombre": "Piccolo",
        "raza": "Namekiano",
        "nivel_pelea": 16000000,
        "tecnicas": ["Final Flash", "Big Bang Attack"],
        "atributos": {"fuerza":120, "defensa":90, "velocidad":89}
        }
    )
    for personaje in personajes:
        print(personaje["nombre"])


def ejercicio2():
    print("\n Ejercicio 2")
    for personaje in personajes:

        velocidad= personaje["atributos"]["velocidad"]                        
        fuerza= personaje["atributos"]["fuerza"]
        resistencia= personaje["atributos" ]["defensa"]    

        media = (velocidad + fuerza + resistencia)/3

        if(media>80):
            print(personaje, "media: ",media)

        
            
def ejercicio3():
    print("\n Ejercicio 3")
    contador =0
    media=0
    for personaje in personajes:

        velocidad= personaje["atributos"]["velocidad"]                          

        media+=velocidad  
        contador+=1

    media/=contador
    print("Media velocidad: ", media)
    for personaje in personajes:
        if(personaje["atributos"]["velocidad"] > media):
            print(personaje)


def ejercicio4():
    print("\n Ejercicio 4")

    for personaje in personajes[:]:
        if "Big Bang Attack" in personaje["tecnicas"]:
            if((personaje["atributos"]["fuerza"]+10)<100):
                personaje["atributos"]["fuerza"]=personaje["atributos"]["fuerza"]+10

                print(personaje["nombre"],personaje["atributos"]["fuerza"])


def ejercicio5():
    print("\n Ejercicio 5")
    for personaje in personajes:
        if(personaje["nombre"] == "Vegeta"):
            vegeta_fuerza=personaje["atributos"]["fuerza"]
            vegeta_defensa=personaje["atributos"]["defensa"]

    for personaje in personajes:
        if(personaje["atributos"]["defensa"]<vegeta_fuerza and personaje["nombre"]!="Vegeta"):
                print(personaje["nombre"],personaje["atributos"]["defensa"])
        


def ejercicio6():
    print("\n Ejercicio 6")
    for personaje in personajes[:]:
        if "Saiyan" in personaje["raza"]:
            personajes.remove(personaje)

    for personaje in personajes:
        print(personaje)

