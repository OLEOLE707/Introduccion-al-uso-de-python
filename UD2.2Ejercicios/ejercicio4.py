num1 = int(input("Introduce un numero: "))

if(num1<0):
    print("Error el numero no puede ser menor que 1")

else: 
    print("La secuencia quedaria como:")
    a = 0
    print(a)
    b = 1
    print(b)
    for i in range(1, num1-1):
        
        resultado=a+b
        a=b
        b=resultado

        print(resultado)