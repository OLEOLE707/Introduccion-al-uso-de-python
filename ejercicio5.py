class Utilidades:
    @staticmethod
    def factorial(a):
        resultado = 1
        for i in range(1, a + 1):
            resultado *= i
        return resultado


filas = int(input("Introduce el numero de filas a mostrar: "))

a = 0
espacios = filas-1

for i in range(0, filas):
    
    for p in range(0, espacios):
        print(" ", end="")
    
    espacios-=1

    for j in range(0, i + 1):
        resultado = Utilidades.factorial(a) / (Utilidades.factorial(j) * Utilidades.factorial(a - j))
        print(int(resultado), end=" ")

    print()
    a+=1