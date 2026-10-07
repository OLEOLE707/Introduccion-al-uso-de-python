base = int(input("Introduce la base: "))
potencia = int(input("Introduce la potencia: "))

if(base<1 or potencia<0):
    print("Error datos incorrectos")
else:
    resultado = base

    for i in range(1,potencia):
        resultado*=base

    print("La potencia de "+str(base)+" es : "+ str(resultado))
