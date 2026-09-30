#5.1
def main():
    #5.2
    frutas = ["Manzana","Pera","Melocoton"]
    
    #5.3
    frutas2 = ["Kiwi","Sandía,","Melón."]
    
    #5.4
    frutas.extend(frutas2)
    
    #5.5
    print(frutas[-1])
    
    #5.6
    tupla = (3,5,7)
    
    #5.7
    print("Primero:", tupla[1])
    
    #5.8
    inicio = int(input("Introduce el inicio: "))
    fin = int(input("Introduce el fin: "))
    salto = int(input("Introduce el salto: "))
    
    rango = range(inicio,fin,salto)
    
    #5.9
    print(rango)

if __name__ == "__main__":
    main()




