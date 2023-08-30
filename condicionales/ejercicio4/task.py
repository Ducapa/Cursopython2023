num=int(input("Introduce un número entero:"))
u= 2
u= num%u
if u != 0:
    print("El número",num,"es impar")
else:
    print("El número",num, "es par")