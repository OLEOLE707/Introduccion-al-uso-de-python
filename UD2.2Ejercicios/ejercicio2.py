num1 = int(input("Introduce un numero: "))

if(num1<1):
    print("Error el numero no puede ser menor que 1")

else: 
    for i in range(1, num1+1):
        resultado = 1
        
        for j in range(1, i+1):
            resultado *= j
        
        print("El factorial de " + str(i) + "! es " + str(resultado))

        i+=1
    
    
        