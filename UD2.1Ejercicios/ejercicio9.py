num = int(input("Ingrese un numero: "))

contador=0

for i in range(1, num+1):
    if num % i == 0:
        contador += 1
        
if(contador == 2):
    print("El numero es primo")
else:
    print("El numero no es primo")
