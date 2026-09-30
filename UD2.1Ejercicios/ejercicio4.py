mmLluvia = float(input("Ingrese la cantidad de lluvia en milímetros: "))

match mmLluvia:
    case x if x == 0:
        print("No ha habido lluvia")
    case x if x < 60:
        print("No hay alerta")
    case x if x >= 60:
        print("Alerta amarilla")
    case x if  x >= 120:
        print("Alerta roja")
    case _:
        print("Valor no válido")


if mmLluvia == 0:
    print("No ha habido lluvia")
elif mmLluvia < 60:
    print("No hay alerta")
elif mmLluvia >= 60:
    print("Alerta amarilla")
elif mmLluvia >= 120:
    print("Alerta roja")
else:
    print("Valor no válido")