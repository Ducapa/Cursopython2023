num=int(input("Introduce un número entero positivo:"))
a=""
for i in range(num,-1,-1):
    a = a + str(i) + ", "
print(a,end="")