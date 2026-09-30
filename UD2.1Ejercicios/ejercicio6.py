contraseña = "12345"

intento = ""

while intento != contraseña:
    intento = input("Introduce la contraseña: ")
    if intento != contraseña:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
    else:
        print("Contraseña correcta.")

