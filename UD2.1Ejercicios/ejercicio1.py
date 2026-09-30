nota = int(input("Ingrese una nota: "))

match nota:
    case x if x < 5:
        print("Supenso")
    case x if x < 7:   
        print("Aprobado")
    case x if x < 9:
        print("Notable")
    case x if x <= 10:
        print("Sobresaliente")