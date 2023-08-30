pala = input("Introduce una palabra:")
reversed_pala = pala
pala = list(pala)
reversed_pala = list(reversed_pala)
reversed_pala.reverse()
if pala == reversed_pala:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")