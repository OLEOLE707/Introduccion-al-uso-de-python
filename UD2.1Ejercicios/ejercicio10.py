num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))


while num1 != num2:
    contador=0

    for i in range(1, num1+1):
        if num1 % i == 0:
            contador += 1
    if(contador == 2):
        print(num1)
    num1+= 1


        

