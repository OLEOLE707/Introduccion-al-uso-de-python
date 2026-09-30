edad = int(input("Ingrese su edad: "))

match edad:
    case x if x < 18:
        print("Eres menor de edad")
    case x if x < 0:   
        print("Error aun no has nacido")
    case x if x >= 18:
        print("Eres mayor de edad")
    case x if x > 120:
        print("Eres un vampiro")