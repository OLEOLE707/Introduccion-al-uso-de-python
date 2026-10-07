num1 = int(input("Introduce un numero: "))

if(num1<0):
    print("Error el numero no puede ser menor que 0")

else: 
    resultado = 0

    for i in range(1, num1+1):
        resultado += i
        i+=1
    
    print("El resultado es ", resultado )
        