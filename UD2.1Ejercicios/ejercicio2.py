precio = float(input("Ingrese el precio del producto: "))
iva = input("Introduce el tipo de IVA (general, reducido o superreducido): ").lower()

if iva == "general":
    precio_final = precio * 1.21
elif iva == "reducido":
    precio_final = precio * 1.10
elif iva == "superreducido":
    precio_final = precio * 1.04
else:
    print("Tipo de IVA no válido")
    precio_final = precio

print("El precio final del producto es:",precio_final)

match iva:
    case "general":
        precio_final = precio * 1.21   
    case "reducido":
        precio_final = precio * 1.10
    case "superreducido":
        precio_final = precio * 1.04
    case _:
        print("Tipo de IVA no válido")  

print("El precio final del producto es:",precio_final)
