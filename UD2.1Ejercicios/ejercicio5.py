num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print("Error: el primer número es mayor que el segundo.")

else:
    if  num1 % 2 != 0:
            num1 += 1
    
    print("for: ")
    for i in range(num1, num2, 2):
        print(i)

    print("while: ")
    while num1 < num2:
        print(num1)
        num1 += 2
        

