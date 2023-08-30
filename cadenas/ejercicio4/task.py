numero=str(input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx:"))
numero=numero.split("-")
print("El número de teléfono es",numero[1])